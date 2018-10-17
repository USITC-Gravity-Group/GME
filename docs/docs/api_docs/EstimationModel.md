## Class
gme.**EstimationModel**(*estimation_data: gme.EstimationData = None, 
                                lhs_var: str = None,
                                rhs_var: List[str] = None,
                                sector_by_sector: bool = False,
                                drop_imp_exp: List[str] = [ ],
                                drop_imp: List[str] = [ ],
                                drop_exp: List[str] = [ ],
                                keep_imp_exp: List[str] = [ ],
                                keep_imp: List[str] = [ ],
                                keep_exp: List[str] = [ ],
                                drop_years: List[str] = [ ],
                                keep_years: List[str] = [ ],
                                drop_missing: bool = True,
                                variables_to_drop_missing: List[str] = None,
                                fixed_effects:List[Union[str,List[str]]] = [ ],
                                omit_fixed_effect:List[Union[str,List[str]]] = ['exporter','exporter-year', 'year'],
                                std_errors:str = 'HC1',
                                iteration_limit:int = 1000,
                                drop_intratrade:bool = False,
                                retain_modified_data:bool = False,
                                full_results:bool = False*)
 
## Description
The class used to specify and run an gravity estimation.  A gme.EstimationData must be supplied along with a collection of largely optional arguments that specify variables to include, fixed effects to create, and how to perform the regression, among other options.  After the definition of the model, additional methods such as .estimate(), which performs the PPML estimation, or .combine_sector_results(), which combines the results for each sector (if applicable) can be called.

## Arguments
**estimation_data**: *gme.EstimationData* <br>
 &emsp; A GME EstimationData to use as the basis of the gravity model. 

**spec_name**: (optional) *str* <br>
 &emsp; A name for the model. 

**lhs_var**: *str* <br>
 &emsp; The column name of the variable to be used as the dependent or 'left-hand-side' variable in the
 &emsp; regression. 
            
**rhs_var**: *List[str]* <br>
 &emsp; A list of column names for the independent or 'right-hand-side' variable(s) to be used in the <br>
 &emsp; regression. 
            
**sector_by_sector**: *bool* <br>
 &emsp; If true, separate models are estimated for each sector, individually.  Default is False. If True, <br>
 &emsp; a sector_var_name must have been supplied to the EstimationData. 
            
**drop_imp_exp**: (optional) *List[str]* <br>
 &emsp; A list of country identifiers to be excluded from the estimation when they appear as an<br> 
 &emsp; importer or exporter. 
            
**drop_imp**: (optional) *List[str]* <br>
 &emsp; A list of country identifiers to be excluded from the estimation when they appear as an <br> 
 &emsp; importer. 
            
**drop_exp**: (optional) *List[str]* <br>
 &emsp; A list of country identifiers to be excluded from the estimation when they appear as an <br> 
 &emsp; exporter. 
            
**keep_imp_exp**: (optional) *List[str]* <br>
 &emsp; A list of countries to include in the estimation as either importers or exporters. All others not <br>
 &emsp; specified are excluded. 
            
**keep_imp**: (optional) *List[str]* <br>
 &emsp; A list of countries to include in the estimation as importers. All others not specified are <br>
 &emsp; excluded. 
            
**keep_exp**: (optional) *List[str]* <br>
 &emsp; A list of countries to include in the estimation as exporters. All others not specified are <br>
 &emsp; excluded. 
            
**drop_years**: (optional) *list* <br>
 &emsp; A list of years to exclude from the estimation. The list elements should match the dtype of <br>
 &emsp; the year column in the EstimationData. 
            
**keep_years**: (optional) *list* <br>
 &emsp; A list of years to include in the estimation. The list elements should match the dtype of the <br>
 &emsp; year column in the EstimationData. 
 
**drop_missing**: *bool* <br>
 &emsp; If True, rows with missing values are dropped. Default is true, which drops if observations <br> 
 &emsp; are missing in any of the columns specified by lhs_var or rhs_var. 
            
**variables_to_drop_missing**: (optional) *List[str]*   <br>
&emsp; A list of column names for specifying which columns to check for missing values when <br> 
&emsp; dropping rows. 

**fixed_effects**: (optional) *List[Union[str,List[str]]]*  <br>
&emsp; A list of variables to construct fixed effects based on. Can accept single string entries, which <br>
&emsp; create fixed effects corresponding to that variable or lists of strings that create fixed effects <br>
&emsp; corresponding to the interaction of the list items. For example, <br> 
&emsp; *fixed_effects = ['importer',['exporter','year']]* would create a set of importer fixed effects <br> 
&emsp; and a set of exporter-year fixed effects. 
            
**omit_fixed_effect**: (optional) *List[Union[str,List[str]]]*<br>
&emsp; The fixed effect category from which to drop a fixed effect to avoid collinearity. The entry <br>
&emsp; should be a subset of the list supplied for fixed_effects. In each case, the last fixed effect <br> 
&emsp; is dropped. If not specified, the colinearity diagnostics will identify a column to drop on its <br> 
&emsp; own. 
            
**std_errors**: (optional) *str*    <br>
 &emsp; Specifies the type of standard errors to be computed. Default is HC1, heteroskedascticity <br> 
 &emsp; robust errors. See [statsmodels documentation](http://www.statsmodels.org/dev/generated/statsmodels.regression.linear_model.RegressionResults.html) for alternative options. 
            
**iteration_limit**: (optional) *int*   <br>
 &emsp; Upper limit on the number of iterations for the estimation procedure. Default is 1000.  

**drop_intratrade**: (optional) *bool*  <br>
&emsp; If True, intra-national trade flows (importer == exporter) are excluded from the regression. <br> 
&emsp; Default is False. 
            
**retain_modified_data**: (optional) *bool*   <br>
 &emsp; If True, the estimation DataFrames for each sector after they have been (potentially) modified<br> 
 &emsp; during the pre-diagnostics for collinearity and convergence issues. Default is False. <br> 
 &emsp; WARNING: these object sizes can be very large in memory so use with caution.  

**full_results**: *bool* <br>
 &emsp; If True, estimate() returns the full results object from the GLM estimation.  These results can <br> 
 &emsp; be quite large as each estimated sector's results will contain a full copy of the data used for <br> 
 &emsp; its estimation, vectors of predicted values, and other memory intensive pieces of data. <br>
 &emsp; If False, estimate() returns a smaller subset of the results that are likely most useful (e.g.  <br> 
 &emsp; .params, .nobs, .bse, .pvalues, .aic, .bic).  For a list of these attributes, see the documentation<br> 
 &emsp; for the function [SlimResults](SlimResults). 

## Attributes
**estimation_data**:<br> 
 &emsp; Return the EstimationData. 

**results_dict**:<br> 
 &emsp; Return the dictionary of regression results (after applying estimate method). 

**modified_data**:<br> 
 &emsp; Return data modified data after removing problematic columns (after applying estimate<br> 
 &emsp; method) 

**ppml_diagnostics**:<br> 
 &emsp; Return PPML estimation diagnostic information (after applying estimate method). See<br>
 &emsp; [estimate](estimate_method.md).  

## Methods
**estimate**:<br> 
 &emsp; Estimate a PPML model. See [estimate](../estimate_technical.md). 

**combine_sector_results**:<br> 
 &emsp; Combine multiple result_dict entries into a single DataFrame. See [combine_sector_results](combine_sector_results.md).   

**format_regression_table**:<br> 
 &emsp; Format regression results into a text, csv, or LaTeX table for presentation. See <br> 
 &emsp; [format_regression_table](format_regression_table.md) 


## Examples
```python
# Declare an EstimationModel
>>> sample_estimation_model = gme.EstimationModel(data_object = gme_data,
...                                              lhs_var = 'trade_value',
...                                              rhs_var = ['log_distance',
...                                              'agree_pta',
...                                              'common_language',
...                                              'contiguity'])

# Estimate the model
>>> sample_estimation_model.estimate()

# Extract the results
>>> results_dictionary = sample_estimation_model.results_dict

# Write the estimates, p-values, and std. errors from all sectors to a .csv file.
>>> sample_estimation_model.combine_sector_results("c:\\folder\\saved_results.csv") 

# Create and export a formatted table of estimation results
>>> sample_estimation_model.format_regression_table(format = 'csv',
...                                                 path = "c:\\folder\\saved_results.csv")

```

