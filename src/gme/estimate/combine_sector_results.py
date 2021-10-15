__author__ = "Peter Herman"
__project__ = "gme.estimate"
__created__ = "04-30-2018"
__all__ = ['combine_sector_results']

import pandas as pd

def combine_sector_results(result_dict:dict = None,
                            write_path:str = None,
                            significance_stars: bool = False,
                            round_results: int = None,
                            latex_syntax: bool = False):
    '''
    Extract key result fields (coefficients, standard errors, and p-values) and combine them in a DataFrame. Has the option to write the data to a .csv file.
    Args:
        result_dict: Dict[statsmodels.genmod.generalized_linear_model.GLMResultsWrapper]
            A dictionary of GLM fit objects as returned by gme.EsimationModel.estimate()
        write_path: (optional) str
            A system location and file name in which to write a csv file containing the combined results.
        significance_stars: bool
            If true, combined results are output with significance stars. *** <0.01, **<0.05, and *<0.10. Default is False.
        round_results: (optional) int
            Rounds combined results to the desired decimal place.
        latex_syntax: bool
            If True, reports aspects of results, such as significance stars, using standard latex syntax.

    Returns: Pandas.DataFrame
        A DataFrame containing combined GLM results for all results in the supplied dictionary.

    Examples:
        # Using a gme.EstimationModel named sample_model...
        >>> sample_results = sample_model.estimate()
        >>> combine_sector_results(sample_results)
                                  all_coeff     all_pvalue              all_stderr
        log_distance              -0.739840  9.318804e-211  (0.023879411125052336)
        agree_pta                  0.334219   5.134355e-15   (0.04271952339258154)
        common_language            0.128770   1.076932e-03   (0.03938367074719932)
        contiguity                 0.255161   5.857612e-08   (0.04705076644539403)
        importer_year_fe_ARG2013  26.980367   0.000000e+00    (0.3612289201097519)

        >>> combine_sector_results(sample_results, path = 'c:\\Documents\\combined_results_saved.csv')
    '''


    keys = result_dict.keys()
    columns = []
    for column_name in keys:
        names = (str(column_name) + '_coeff',str(column_name) + '_stderr',str(column_name) + '_pvalue')
        sector = pd.DataFrame({
            names[0]: result_dict[column_name].params,
            names[1]: result_dict[column_name].bse,
            names[2]: result_dict[column_name].pvalues})

        one_percent = sector[names[2]] < 0.01
        five_percent = (sector[names[2]] < 0.05) & (sector[names[2]] >= 0.01)
        ten_percent = (sector[names[2]] < 0.1) & (sector[names[2]] >= 0.05)

        if round_results is not None:
            sector = sector.round(round_results)

        if significance_stars is True:
            if latex_syntax is True:
                sector.loc[one_percent, names[0]] = (sector[names[0]].astype(str) + '$^{***}$')
                sector.loc[five_percent, names[0]] = (sector[names[0]].astype(str) + '$^{**}$')
                sector.loc[ten_percent, names[0]] = (sector[names[0]].astype(str) + '$^{*}$')
            else:
                sector.loc[one_percent, names[0]] = (sector[names[0]].astype(str) + '***')
                sector.loc[five_percent, names[0]] = (sector[names[0]].astype(str) + '**')
                sector.loc[ten_percent, names[0]] = (sector[names[0]].astype(str) + '*')

        if latex_syntax is True:
            if round_results is not None:  # Rounding and converting to a string loses trailing zeros, this re-adds them
                sector[names[1]] = sector[names[1]].astype(str)
                lost_zero = (sector[names[1]].str.len() - sector[names[1]].str.index('.') - 1) < round_results
                sector.loc[lost_zero, names[1]] = (sector[names[1]] + '0')

            sector[names[1]] = ('(' + sector[names[1]].astype(str) + ')')

        singletons = {'nobs':result_dict[column_name].nobs,
                      'aic':result_dict[column_name].aic,
                      'bic': result_dict[column_name].bic,
                      'likelihood':result_dict[column_name].llf}

        for key in singletons.keys():
            new_row = pd.DataFrame({
            names[0]: singletons[key],
            names[1]: singletons[key],
            names[2]: singletons[key]}, index = [key])
            if round_results is not None:
                new_row = new_row.round(round_results)

            sector = pd.concat([sector,new_row], axis = 0)

        columns.append(sector)
    combined_sectors = pd.concat(columns, axis = 1)

    if write_path is not None:
        combined_sectors.to_csv(write_path)

    return combined_sectors