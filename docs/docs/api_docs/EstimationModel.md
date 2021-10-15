## Class
gme.<strong>EstimationModel</strong>(<em>estimation_data: gme.EstimationData = None, 
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
                                full_results:bool = False</em>)
 
## Description
The class used to specify and run an gravity estimation.  A gme.EstimationData must be supplied along with a collection of largely optional arguments that specify variables to include, fixed effects to create, and how to perform the regression, among other options.  After the definition of the model, additional methods such as <em>estimate</em>, which performs the PPML estimation, or <em>combine_sector_results</em>, which combines the results for each sector (if applicable) can be called.

## Arguments
<dl>

<dt><strong>estimation_data</strong>: <em>gme.EstimationData</em> </dt>
 <dd><p> A GME EstimationData to use as the basis of the gravity model. </p></dd>

<dt><strong>spec_name</strong>: (optional) <em>str</em> </dt>
 <dd><p> A name for the model. </p></dd>

<dt><strong>lhs_var</strong>: <em>str</em> </dt>
 <dd><p> The column name of the variable to be used as the dependent or 'left-hand-side' variable in the regression. </p></dd>
            
<dt><strong>rhs_var</strong>: <em>List[str]</em> </dt>
 <dd><p> A list of column names for the independent or 'right-hand-side' variable(s) to be used in the regression. </p></dd>
            
<dt><strong>sector_by_sector</strong>: <em>bool</em> </dt>
 <dd><p> If true, separate models are estimated for each sector, individually.  Default is False. If True, a sector_var_name must have been supplied to the EstimationData. </p></dd>
            
<dt><strong>drop_imp_exp</strong>: (optional) <em>List[str]</em> </dt>
 <dd><p> A list of country identifiers to be excluded from the estimation when they appear as an importer or exporter. </p></dd>
            
<dt><strong>drop_imp</strong>: (optional) <em>List[str]</em> </dt>
 <dd><p> A list of country identifiers to be excluded from the estimation when they appear as an importer. </p></dd>
            
<dt><strong>drop_exp</strong>: (optional) <em>List[str]</em> </dt>
 <dd><p> A list of country identifiers to be excluded from the estimation when they appear as an exporter. </p></dd>
            
<dt><strong>keep_imp_exp</strong>: (optional) <em>List[str]</em> </dt>
 <dd><p> A list of countries to include in the estimation as either importers or exporters. All others not specified are excluded. </p></dd>
            
<dt><strong>keep_imp</strong>: (optional) <em>List[str]</em> </dt>
 <dd><p> A list of countries to include in the estimation as importers. All others not specified are excluded. </p></dd>
            
<dt><strong>keep_exp</strong>: (optional) <em>List[str]</em> </dt>
 <dd><p> A list of countries to include in the estimation as exporters. All others not specified are excluded. </p></dd>
            
<dt><strong>drop_years</strong>: (optional) <em>list</em> </dt>
 <dd><p> A list of years to exclude from the estimation. The list elements should match the dtype of the year column in the EstimationData. </p></dd>
            
<dt><strong>keep_years</strong>: (optional) <em>list</em> </dt>
 <dd><p> A list of years to include in the estimation. The list elements should match the dtype of the year column in the EstimationData. </p></dd>
 
<dt><strong>drop_missing</strong>: <em>bool</em> </dt>
 <dd><p> If True, rows with missing values are dropped. Default is true, which drops if observations are missing in any of the columns specified by lhs_var or rhs_var. </p></dd>
            
<dt><strong>variables_to_drop_missing</strong>: (optional) <em>List[str]</em>  </dt> 
<dd><p> A list of column names for specifying which columns to check for missing values when dropping rows. </p></dd>

<dt><strong>fixed_effects</strong>: (optional) <em>List[Union[str,List[str]]]</em>  </dt>
<dd><p> A list of variables to construct fixed effects based on. Can accept single string entries, which create fixed effects corresponding to that variable or lists of strings that create fixed effects corresponding to the interaction of the list items. For example, <em>fixed_effects = ['importer',['exporter','year']]</em> would create a set of importer fixed effects and a set of exporter-year fixed effects. </p></dd>
            
<dt><strong>omit_fixed_effect</strong>: <em> (optional) Dict[Union[str,Tuple[str]]:List[str, Tuple[str]]]</em> </dt>
<dd><p> A dictionary of fixed effect categories and values to be dropped from dataframe. The dictionary key(s) can be either a single string corresponding to one dimension of the fixed effects or a tuple of strings specifying multiple dimensions. The values should then be either a list of strings for 1 dimension or a list of tuples for multiple dimensions. For example, {'importer':['DEU', 'ZAF'], 'exporter':['USA']} or {('importer','year'):[('ARG','2015'),('BEL','2013')]}. The fixed effect categories in the keys need to be a subset of the list supplied for fixed_effects. If not specified, the collinearity diagnostics will identify a column to drop on its own. 

</p>
<p>

<em>(Version 1.2 or earlier)</em>: <strong>omit_fixed_effect</strong>: (optional) <em>List[Union[str,List[str]]]</em>
 The fixed effect category from which to drop a fixed effect to avoid collinearity. The entry 
 should be a subset of the list supplied for fixed_effects. In each case, the last fixed effect  
 is dropped. If not specified, the colinearity diagnostics will identify a column to drop on its  
 own. 
 </p>
</dd>

</dl>



<dl>            
<dt><strong>std_errors</strong>: (optional) <em>str</em></dt>    
 <dd><p> Specifies the type of standard errors to be computed. Default is HC1, heteroskedascticity robust errors. See [statsmodels documentation](http://www.statsmodels.org/dev/generated/statsmodels.regression.linear_model.RegressionResults.html) for alternative options. </p></dd>
            
<dt><strong>iteration_limit</strong>: (optional) <em>int</em> </dt>  
 <dd><p> Upper limit on the number of iterations for the estimation procedure. Default is 1000. </p></dd> 

<dt><strong>drop_intratrade</strong>: (optional) <em>bool</em> </dt> 
<dd><p> If True, intra-national trade flows (importer == exporter) are excluded from the regression. Default is False. </p></dd>
            
<dt><strong>retain_modified_data</strong>: (optional) <em>bool</em> </dt>  
<dd><p>  If True, the estimation DataFrames for each sector after they have been (potentially) modified during the pre-diagnostics for collinearity and convergence issues. Default is False. WARNING: these object sizes can be very large in memory so use with caution.  </p></dd>

<dt><strong>full_results</strong>: <em>bool</em> </dt>
 <dd><p> If True, estimate() returns the full results object from the GLM estimation.  These results can be quite large as each estimated sector's results will contain a full copy of the data used for its estimation, vectors of predicted values, and other memory intensive pieces of data. If False, estimate() returns a smaller subset of the results that are likely most useful (e.g. .params, .nobs, .bse, .pvalues, .aic, .bic). For a list of these attributes, see the documentation for the function [SlimResults](SlimResults). </p></dd>
 
<dt><strong>cluster_on</strong>: <em>(optional) str</em></dt>
 <dd><p> The name of a column of categorical variables to use as clusters for clustered standard errors.</p></dd>
</dl>



## Attributes
<dl>
<dt><strong>estimation_data</strong>:</dt> 
  <dd><p>Return the EstimationData.</p></dd> 

<dt><strong>results_dict</strong>: </dt>
  <dd><p>Return the dictionary of regression results (after applying estimate method).</p></dd> 

<dt><strong>modified_data</strong>: </dt>
  <dd><p>Return data modified data after removing problematic columns (after applying estimate method) </p></dd>

<dt><strong>ppml_diagnostics</strong>: </dt>
  <dd><p>Return PPML estimation diagnostic information (after applying estimate method). See [estimate](estimate_method.md).</p></dd> 
 </dl>


## Methods
<dl>
<dt><strong>estimate</strong>:</dt> 
  Estimate a PPML model. See [estimate](../estimate_technical.md). 

<dt><strong>combine_sector_results</strong>: </dt>
  Combine multiple result_dict entries into a single DataFrame. See [combine_sector_results](combine_sector_results.md).   

<dt><strong>format_regression_table</strong>: </dt>
  Format regression results into a text, csv, or LaTeX table for presentation. See  
  [format_regression_table](format_regression_table.md) 
</dl>

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

# Define a model with fixed effects and drop specific ones
            >>> fe_model = EstimationModel(est_data,
                                           lhs_var='trade_value',
                                           rhs_var=grav_vars,
                                           fixed_effects=[['importer', 'year'], ['exporter', 'year']],
                                           omit_fixed_effect={('importer','year'):[('DEU','2015')],'exporter':['USA']})
```

