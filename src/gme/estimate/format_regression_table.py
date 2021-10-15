__author__ = "Peter Herman"
__project__ = "gme.estimate"
__created__ = "05-07-2018"
__all__ = ['format_regression_table']
from typing import List
import pandas as pd


def format_regression_table(results_dict: dict = None,
                            variable_list: List[str] = [],
                            format: str = 'txt',
                            se_below: bool = True,
                            significance_levels: List[float] = [0.01, 0.05, 0.10],
                            round_values: int = 3,
                            omit_fe_prefix: List[str] = [],
                            table_columns: list = [],
                            path: str = None,
                            include_index: bool = False,
                            latex_syntax: bool = False,
                            r_squared: bool = False,
                            note: str = None):
    '''
    Format estimation results into a standard table format with options for significance stars, LaTeX syntax, standard
    error positioning, rounding, fixed effect ommission, and others options.

    Args:
        results_dict: Dict[statsmodels.genmod.generalized_linear_model.GLMResultsWrapper]
            A dictionary of GLM fit objects from statsmodels
        variable_list: (optional) List[str]
            A list of variables to include in the results table. If none are provided, all variables are included. The
            default is an empty list, which results in the inclusion of all estimated variables.
        format: str
            Determines the file formatting of text. Accepts 'tex' for LaTeX, 'txt' for plain text, or 'csv' for a
            csv table. Default is 'txt'.
        se_below: bool
            If True, standard errors are presented below estimates. If False, they are presented in a column to the
            right. The default is True.
        significance_levels: List[float]
            A list specifying the three percentages, from lowest to highest, on which to base significance stars. The
            default value is [0.01, 0.05, 0.10].
        round_values: int
            The number of decimal points to include in the reported figures. The default is 3.
        omit_fe_prefix: (optional) List[str]
            A list of strings such that any variable starting with that string are omitted from the created table. The
            value is an empty list that omits no variables.
        table_columns: (optional) List[str]
            A list of keys from the results_dict to be included in the created table. The default is an empty list, which
            results in all values being created
        path: (optional) str
            A system path and file name to write the created table to.  File extensions of .txt (format = 'txt'),
            .tex or .txt (format = 'tex'), or .csv (format = 'csv') are recommended.
        include_index: bool
            If true, the outputed .csv file will contain row numbers. Default is False.
        latex_syntax: bool
            If true, the table will include LaTeX syntax, regardless of the chosen format. Default is False
        variable_order: (optional) List[str]
            If supplied, provides an specific ordering in which to list the variables in the table.
        r_squared:  bool
            If True, it includes R^2 values in the table. This is primarily useful if OLS regression results are
            supplied. Default is False.
        note: (optional) str
            Adds the supplied string as a note at the bottom of the table.

    Returns: Pandas.DataFrame
        A DataFrame containing the formatted results table with specified syntax.

    Examples:
        Create a .csv file.
        >>> sample_estimation_model.format_regression_table(format = 'csv',
                                                            path = "c:\folder\saved_results.csv")

        Create a LaTeX .tex table without fixed effects (with prefix 'imp_fe_' and 'exp_fe_')
        >>> sample_estimation_model.format_regression_table(format = 'tex',
                                                            path = "c:\folder\saved_results.tex",
                                                            omit_fe_prefix = ['imp_fe_' , 'exp_fe_'])
    '''

    if results_dict is None:
        raise ValueError('Must input a dictionary of regression (GLM.fit) objects')

    if len(table_columns) == 0:
        table_columns = list(results_dict.keys())
    else:
        for column in table_columns:
            if column not in list(results_dict.keys()):
                raise ValueError('Specified column {0} in table_columns is not a key in results_dict.'.format(column))

    formatted_dict = {}
    for key in table_columns:

        results = results_dict[key]
        if se_below is True:
            compiled_results = pd.DataFrame(columns=['Variable', str(key)])
        if se_below is False:
            compiled_results = pd.DataFrame(columns=['Variable', str(key), (str(key) + ' SE')])

        if len(variable_list) == 0:
            variable_list_current = results.params.index
        else:
            variable_list_current = pd.Series(variable_list)

        if len(omit_fe_prefix) > 0:
            for prefix in omit_fe_prefix:
                variable_list_current = variable_list_current[~variable_list_current.str.startswith(prefix)]

        for variable in variable_list_current:

            # Add significance stars to coefficient
            beta = str(round(results.params[variable], round_values))
            while (len(beta) - beta.index('.') - 1) < round_values:  # pad trailing zeros if dropped
                beta = beta + '0'
            if format == 'tex' or latex_syntax is True:
                if results.pvalues[variable] < significance_levels[0]:
                    formatted_coeff = beta + '$^{***}$'
                if (results.pvalues[variable] < significance_levels[1]) & \
                        (results.pvalues[variable] >= significance_levels[0]):
                    formatted_coeff = beta + '$^{**}$'
                if (results.pvalues[variable] < significance_levels[2]) & \
                        (results.pvalues[variable] >= significance_levels[1]):
                    formatted_coeff = beta + '$^{*}$'
                if results.pvalues[variable] >= significance_levels[2]:
                    formatted_coeff = beta
            else:
                if results.pvalues[variable] < significance_levels[0]:
                    formatted_coeff = beta + '***'
                if (results.pvalues[variable] < significance_levels[1]) & \
                        (results.pvalues[variable] >= significance_levels[0]):
                    formatted_coeff = beta + '**'
                if (results.pvalues[variable] < significance_levels[2]) & \
                        (results.pvalues[variable] >= significance_levels[1]):
                    formatted_coeff = beta + '*'
                if results.pvalues[variable] >= significance_levels[2]:
                    formatted_coeff = beta

            # Format standard error
            std_err = str(round(results.bse[variable], round_values))
            while (len(std_err) - std_err.index('.') - 1) < round_values:  # pad trailing zeros if dropped
                std_err = std_err + '0'
            formatted_se = '(' + std_err + ')'

            if se_below is False:
                row = pd.DataFrame({'Variable': variable,
                                    str(key): formatted_coeff,
                                    (str(key) + ' SE'): formatted_se},
                                   index=[('a_' + variable)])
                compiled_results = pd.concat([compiled_results, row], axis=0)

            if se_below is True:
                row = pd.DataFrame({'Variable': [variable, ' '], str(key): [formatted_coeff, formatted_se]},
                                   index=['a_' + variable, 'a_' + str(variable) + '_se'])
                compiled_results = pd.concat([compiled_results, row], axis=0)

        # GEE models used for cluster option do not report some stats so must catch it and replace with something else
        try:
            num_obs = str(int(results.nobs))
            aic = str(round(results.aic, round_values))
            bic = str(round(results.bic, round_values))
            llf = str(round(results.llf, round_values))
        except:
            num_obs = 'Not reported for model type'
            aic = num_obs
            bic = num_obs
            llf = num_obs
        if se_below is False:
            row = pd.DataFrame({'Variable': ['Obs.', 'AIC', 'BIC', 'Likelihood'],
                                str(key): [num_obs,
                                           aic,
                                           bic,
                                           llf],
                                (str(key) + ' SE'): ['', '', '', '']},
                               index=['b_nobs', 'b_aic', 'b_bic', 'b_llf'])
            if r_squared is True:
                row_r_squared = pd.DataFrame({'Variable': ['R^2'],
                                              str(key): [str(round(results.rsquared, 4))],
                                              (str(key) + ' SE'): ['']},
                                             index=['b_R2'])
                row = pd.concat([row, row_r_squared], axis=0)

        if se_below is True:
            row = pd.DataFrame({'Variable': ['Obs.', 'AIC', 'BIC', 'Likelihood'],
                                str(key): [num_obs,
                                           aic,
                                           bic,
                                           llf]},
                               index=['b_nobs', 'b_aic', 'b_bic', 'b_llf'])
            if r_squared is True:
                row_r_squared = pd.DataFrame({'Variable': ['R^2'],
                                              str(key): [str(round(results.rsquared, 4))]},
                                             index=['b_R2'])
                row = pd.concat([row, row_r_squared], axis=0)

        compiled_results = pd.concat([compiled_results, row], axis=0)

        formatted_dict[key] = compiled_results

    results_table = formatted_dict[table_columns[0]]
    remaining_columns = table_columns[1:]
    for key in remaining_columns:
        results_table = results_table.merge(right=formatted_dict[key], how='outer', left_index=True, right_index=True)
        missing_var_name = results_table['Variable_x'].isnull()
        results_table.loc[missing_var_name, 'Variable_x'] = results_table['Variable_y']
        results_table.drop(['Variable_y'], axis=1, inplace=True)
        results_table.rename(columns={'Variable_x': 'Variable'}, inplace=True)

    results_table.sort_index(inplace=True)

    # Idea: custom sort order for variables

    results_table[results_table.isnull()] = ''

    # Reorder 'Variable' column first
    column_names = results_table.columns.tolist()
    column_names.insert(0, column_names.pop(column_names.index('Variable')))
    results_table = results_table[column_names]
    if path is not None:
        if format == 'tex':
            column_spec = '{' + results_table.shape[1] * 'l' + '}'
            begin_tab = '\\begin{tabular}' + column_spec
            end_tab = '\\end{tabular}'
            results_table.to_csv(path, index=include_index, sep='&', line_terminator='\\\\\n')
            with open(path, 'r+') as file:
                content = file.read()
                content = content.replace('_', '\\_')
                file.seek(0, 0)
                file.write(begin_tab.rstrip('\r\n') + '\n' + content)
            with open(path, 'a+') as file:
                file.write(end_tab)

        if format == 'txt':
            with open(path, 'w') as file:
                file.write(results_table.to_string(index=include_index, justify='left'))

        if format == 'csv':
            results_table.to_csv(path, index=include_index, sep=',', line_terminator='\n')

        # Add note
        footnote = '*** p < {}, ** p < {}, * p < {}. '.format(significance_levels[0], significance_levels[1],
                                                              significance_levels[2])
        with open(path, 'a+') as file:
            if format == 'csv':
                file.write('\n"{}"'.format(footnote))
                if note is not None:
                    file.write('"{}"'.format(note))
            else:
                file.write("\n{}".format(footnote))
                if note is not None:
                    file.write(note)

    return results_table
