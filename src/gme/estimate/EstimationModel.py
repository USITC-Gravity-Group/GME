__Author__ = "Peter Herman"
__Project__ = "Gravity Code"
__Created__ = "03/12/2018"
__all__ = ['EstimationModel']

from typing import List,Tuple, Dict
from typing import Union
from .Specification import Specification
from .DiagnosticsLog import DiagnosticsLog
from .combine_sector_results import combine_sector_results
from ._slice_data_for_estimation import _slice_data_for_estimation
from ._ppml_estimation_and_diagnostics import _estimate_ppml
from .format_regression_table import format_regression_table
from .SlimResults import SlimResults


class EstimationModel(object):
    def __init__(self,
                 estimation_data=None,
                 spec_name: str = 'default_name',
                 lhs_var: str = None,
                 rhs_var: List[str] = [],
                 sector_by_sector: bool = False,
                 drop_imp_exp: List[str] = [],
                 drop_imp: List[str] = [],
                 drop_exp: List[str] = [],
                 keep_imp_exp: List[str] = [],
                 keep_imp: List[str] = [],
                 keep_exp: List[str] = [],
                 drop_years: List[str] = [],
                 keep_years: List[str] = [],
                 drop_missing: bool = True,
                 variables_to_drop_missing: List[str] = None,
                 fixed_effects: List[Union[str, List[str]]] = [],
                 omit_fixed_effect: Dict[Union[str, Tuple[str]],List[Union[str, Tuple[str]]]] = {},
                 std_errors: str = 'HC1',
                 iteration_limit: int = 1000,
                 drop_intratrade: bool = False,
                 retain_modified_data: bool = True,
                 full_results: bool = True,
                 cluster_on: str=None):
        '''
        The GME object is used to specify and run an gravity estimation.  A gme.EstimationData must be supplied along with a
        collection of largely optional arguments that specify variables to include, fixed effects to create, and how
        to perform the regression, among other options.  After the definition of the model, additional methods such as
        .estimate(), which performs the PPML estimation, or .combine_sector_results(), which combines the results for
        each sector (if applicable) can be called.

        Args:
            estimation_data: gme.EstimationData
                A GME EstimationData to use as the basis of the gravity model.
            spec_name: (optional) str
                A name for the model.
            lhs_var: str
                The column name of the variable to be used as the dependent or 'left-hand-side' variable in the
                regression.
            rhs_var: List[str]
                A list of column names for the independent or 'right-hand-side' variable(s) to be used in the regression.
            sector_by_sector: bool
                If true, separate models are estimated for each sector, individually.  Default is False. If True, a
                sector_var_name must have been supplied to the EstimationData.
            drop_imp_exp: (optional) List[str]
                A list of country identifiers to be excluded from the estimation when they appear as an importer or
                exporter
            drop_imp: (optional) List[str]
                A list of country identifiers to be excluded from the estimation when they appear as an importer
            drop_exp: (optional) List[str]
                A list of country identifiers to be excluded from the estimation when they appear as an exporter
            keep_imp_exp: (optional) List[str]
                A list of countries to include in the estimation as either importers or exporters. All others not
                specified are excluded.
            keep_imp: (optional) List[str]
                A list of countries to include in the estimation as importers. All others not specified are excluded.
            keep_exp: (optional) List[str]
                A list of countries to include in the estimation as exporters. All others not specified are excluded.
            drop_years: (optional) list
                A list of years to exclude from the estimation. The list elements should match the dtype of the year
                column in the EstimationData.
            keep_years: (optional) list
                A list of years to include in the estimation. The list elements should match the dtype of the year
                column in the EstimationData.
            drop_missing: bool
                If True, rows with missing values are dropped. Default is true, which drops if observations are missing
                in any of the columns specified by lhs_var or rhs_var.
            variables_to_drop_missing: (optional) List[str]
                A list of column names for specifying which columns to check for missing values when dropping rows.
            fixed_effects: (optional) List[Union[str,List[str]]]
                A list of variables to construct fixed effects based on. Can accept single string entries, which create
                fixed effects corresponding to that variable or lists of strings that create fixed effects corresponding
                to the interaction of the list items. For example, fixed_effects = ['importer',['exporter','year']]
                would create a set of importer fixed effects and a set of exporter-year fixed effects.
            omit_fixed_effect: (optional) Dict[Union[str,Tuple[str]]:List[str, Tuple[str]]]
                A dictionary of fixed effect categories and values to be dropped from dataframe. The dictionary key(s)
                can be either a single string corresponding to one dimension of the fixed effects or a tuple of strings
                specifying multiple dimesions. The values should then be either a list of strings for 1 dimension or a
                list of tuples for multiple dimensions. For example: {'importer':['DEU', 'ZAF'], 'exporter':['USA']} or
                {('importer','year'):[('ARG','2015'),('BEL','2013')]}
                The fixed effect categories in the keys need to be a subset of the list supplied for fixed_effects.
                If not specified, the colinearity diagnostics will identify a column to drop on its own.
            std_errors: (optional) str
                Specifies the type of standard errors to be computed. Default is HC1, heteroskedascticity robust errors.
                See http://www.statsmodels.org/dev/generated/statsmodels.regression.linear_model.RegressionResults.html
                for alternative options.
            iteration_limit: (optional) int
                Upper limit on the number of iterations for the estimation procedure. Default is 1000.
            drop_intratrade: (optional) bool
                If True, intra-national trade flows (importer == exporter) are excluded from the regression. Default is
                False.
            retain_modified_data: (optional) bool
                If True, the estimation DataFrames for each sector after they have been (potentially) modified during
                the pre-diagnostics for collinearity and convergence issues. Default is False. WARNING: these object
                sizes can be very large in memory so use with caution.
            full_results: bool
                If True, estimate() returns the full results object from the GLM estimation.  These results can be quite
                large as each estimated sector's results will contain a full copy of the data used for its estimation,
                vectors of predicted values, and other memory intensive pieces of data.  If False, estimate() returns
                a smaller subset of the results that are likely most useful (e.g. .params, .nobs, .bse, .pvalues, .aic,
                .bic).  For a list of these attributes, see the documentation for the function SlimResults
            cluster_on: (optional) str
                The name of a column of categorical variables to use as clusters for clustered standard errors.

        Attributes:
            estimation_data: Return the EstimationData.
            results_dict: Return the dictionary of regression results (after applying estimate method).
            modified_data: Return data modified data after removing problematic columns (after applying estimate method)
            ppml_diagnostics: Return PPML estimation diagnostic information (after applying estimate method)


        Methods:
            estimate: Estimate a PPML model.
            combine_sector_results: Combine multiple result_dict entries into a single DataFrame.
            format_regression_table: Format regression results into a text, csv, or LaTeX table for presentation.


        Examples:
            Declare an EstimationModel
             >>> sample_estimation_model = EstimationModel(estimation_data = gme_data,
             ...                                           lhs_var = 'trade_value',
             ...                                           rhs_var = ['log_distance',
             ...                                           'agree_pta',
             ...                                           'common_language',
             ...                                           'contiguity'])
            Estimate the model
            >>> sample_estimation_model.estimate("ppml")

            Extract the results
            >>> results_dictionary = sample_estimation_model.results_dict

            Write the estimates, p-values, and std. errors from all sectors to a .csv file.
            >>> sample_estimation_model.combine_sector_results("c:\\folder\\saved_results.csv")

            Create and export a formatted table of estimation results
            >>> sample_estimation_model.format_regression_table(format = 'csv',
            ...                                                 path = "c:\\folder\\saved_results.csv")

            Define a model with fixed effects and drop specific ones
            >>> fe_model = EstimationModel(est_data,
                                           lhs_var='trade_value',
                                           rhs_var=grav_vars,
                                           fixed_effects=[['importer', 'year'], ['exporter', 'year']],
                                           omit_fixed_effect={('importer','year'):[('DEU','2015')],'exporter':['USA']})

        '''

        # Value checks for inputs
        if estimation_data is None:
            raise ValueError("A EstimationData must be provided.")

        if cluster_on is not None and not isinstance(cluster_on, str):
            raise ValueError("cluster_on must be a string indicating the column to cluster on.")

        if not isinstance(omit_fixed_effect, dict):
            raise ValueError("As of gme v1.3, omit_fixed_effect argument must be a dictionary.")

        ##############
        # Attributes #
        ##############
        if (variables_to_drop_missing is None) & (drop_missing):
            variables_to_drop_missing = [lhs_var] + rhs_var
        self.estimation_data = estimation_data
        self.data_log = estimation_data.data_log

        # Create indicator for clustering
        if cluster_on is not None:
            cluster = True
        else:
            cluster = False

        self.specification = Specification(spec_name=spec_name,
                                           lhs_var=lhs_var,
                                           rhs_var=rhs_var,
                                           sector_by_sector=sector_by_sector,
                                           drop_imp_exp=drop_imp_exp,
                                           drop_imp=drop_imp,
                                           drop_exp=drop_exp,
                                           keep_imp_exp=keep_imp_exp,
                                           keep_imp=keep_imp,
                                           keep_exp=keep_exp,
                                           drop_years=drop_years,
                                           keep_years=keep_years,
                                           drop_missing=drop_missing,
                                           variables_to_drop_missing=variables_to_drop_missing,
                                           fixed_effects=fixed_effects,
                                           omit_fixed_effect=omit_fixed_effect,
                                           std_errors=std_errors,
                                           iteration_limit=iteration_limit,
                                           drop_intratrade=drop_intratrade,
                                           cluster=cluster,
                                           cluster_on=cluster_on,
                                           verbose=False)
        self.retain_modified_data = retain_modified_data
        self.full_results = full_results
        self.results_dict = None
        self.modified_data = None
        self.diagnostics_log = DiagnosticsLog(spec_name=spec_name)
        self.ppml_diagnostics = None

    ###########
    # Methods #
    ###########

    def estimate(self):
        '''
        Perform sector by sector GLM estimation with PPML diagnostics. The routine follows several steps.
        services. If sector_by_sector is specified, the routine is repeated for each sector.

        1. Create Fixed effects: Fixed effects are created based on the EstimationModel specification.

        2. Pre-Diagnostics: Several steps are taken to increase the likelihood that the estimation will converge
            successfully.
            a. Perfect Colinearity: Columns and observations that are perfectly collinear are identified and
                excluded.
            b. Insufficient Variation: Fixed effects categories in which there is an insufficient level of
                variation for estimation are excluded.

        3. Estimate: A GLM, PPML estimation is run.

        4. Post-Diagnostics: A test for over-fit values is conducted.

        The method returns one object and stores three in the EstimationModel.  The first object, which is
        both returned and stored as EstimationModel.results_dict is

        Returns: Dict[statsmodels.genmod.generalized_linear_model.GLMResultsWrapper]
            The primary return is a dictionary of results objects from the statsmodels GLM.fit routine, each keyed using
            either the name of the sector if the estimation was sector by sector (i.e. sector_by_sector = True) or with
            the key 'all' if not.

            Additionally, the method assigns two or three attributes of the Estimation model:
                1. EstimationModel.results_dict:  Dict[statsmodels.genmod.generalized_linear_model.GLMResultsWrapper]
                    A copy of the returned dictionary of results, as described above, is stored with the EstimationModel
                2. EstimationModel.ppml_diagnostics: pandas.core.frame.DataFrame
                    A data frame containing a column of pre- and post-diagnostic information for each regression
                3. EstimationModel.modified_data: (optional) Dict[pandas.core.frame.DataFrame]
                    A dictionary using the same keys as results_dict, each containing the modified dataframes created
                    during the pre-diagnostic stages of the estimations. Because of the large memory footprint of this
                    assignment, it is only done if specified (i.e. EstimationModel.retain_modified_data = True)

        Examples:
            >>> sample_estimation_model.estimate("ppml")
        '''
        data_object = self.estimation_data
        specification = self.specification
        data_log = data_object.data_log
        data_frame = data_object.data_frame
        meta_data = data_object.meta_data
        diagnostics_log = self.diagnostics_log

        if specification.sector_by_sector is True and meta_data.sector_var_name is None:
            raise ValueError('sector_var_name must be specified for sector_by_sector option')

        estimation_data_frame, data_log = _slice_data_for_estimation(data_frame=data_frame,
                                                                      specification=specification,
                                                                      meta_data=meta_data,
                                                                      data_log=data_log)

        results_dict, ppml_diagnostics, modified_data \
            = _estimate_ppml(data_frame=estimation_data_frame,
                             meta_data=meta_data,
                             specification=specification,
                             fixed_effects=specification.fixed_effects,
                             drop_fixed_effect=specification.omit_fixed_effect,
                             cluster=specification.cluster,
                             cluster_on=specification.cluster_on)

        self.ppml_diagnostics = ppml_diagnostics
        if self.retain_modified_data:
            self.modified_data = modified_data

        if self.full_results:
            self.results_dict = results_dict
        else:
            slim_results_dict = {}
            for key in results_dict:
                slim_results_dict[key] = SlimResults(results_dict[key])
            self.results_dict = slim_results_dict


        

        return self.results_dict

    def combine_sector_results(self,
                               write_path: str = None):
        '''
        Combines all results in the results_dict into a single data_frame, retaining estimated coefficients, standard
        errors, and p-values.

        See combine_sector_results() function for more details.

        Examples:
            Create a new DataFrame with results.
            >>> combined_results = sample_estimation_model.combine_sector_results()

            Write to combined results to a .csv file.
            >>> sample_estimation_model.combine_sector_results("c:\folder\saved_results.csv")

            Or do both.
            >>> combined_results = sample_estimation_model.combine_sector_results("c:\folder\saved_results.csv")

        '''
        if self.results_dict is None:
            raise ValueError('EstimationModel must be estimated first (EstimationModel.results_dict cannot be None)')
        return combine_sector_results(self.results_dict, write_path)

    # Commented out until it can be debugged
    # def pickle_model(self,
    #               write_path: str = None):
    #    '''
    #    '''
    #    Save an EstimationModel as a python-readable object (pickle) at a specified location.
    #    Args:
    #        write_path: (str)
    #            The location (including file name) to write the EstimationModel object
    #
    #    Examples:
    #        Save the EstimationModel.
    #        >>> sample_estimation_model.pickle_model("c:\folder\saved_object.p")
    #        Reload the model.
    #        >>> import pickle
    #        >>> loaded_model = pickle.load( open("c:\folder\saved_object.p"))
    #    '''
    #    '''
    #    if write_path is None:
    #        raise ValueError("write_path must be specified.")
    #
    #    pickle.dump(self, open(write_path, "wb"))
    #    '''

    def format_regression_table(self,
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
                                note:str = None
                                ):
        '''
        Format estimation results into a table with significance stars, rounded values, etc. The EstimationModel method
        is a shortcut to the stand-alone function. See the function gme.estimate.format_regression_table for more
        details.

        See format_regression_table() function definition for details.

        Examples:
            Create a .csv file.
            >>> sample_estimation_model.format_regression_table(format = 'csv',
                                                                path = "c:\folder\saved_results.csv")

            Create a LaTeX .tex table without fixed effects (with prefix 'imp_fe_' and 'exp_fe_')
            >>> sample_estimation_model.format_regression_table(format = 'tex',
                                                                path = "c:\folder\saved_results.tex",
                                                                omit_fe_prefix = ['imp_fe_' , 'exp_fe_'])
        '''
        return format_regression_table(results_dict=self.results_dict,
                                       variable_list=variable_list,
                                       format=format,
                                       se_below=se_below,
                                       significance_levels=significance_levels,
                                       round_values=round_values,
                                       omit_fe_prefix=omit_fe_prefix,
                                       table_columns=table_columns,
                                       path=path,
                                       include_index=include_index,
                                       latex_syntax=latex_syntax,
                                       r_squared=r_squared,
                                       note = note)



