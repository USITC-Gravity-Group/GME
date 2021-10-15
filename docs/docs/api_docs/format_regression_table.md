## Function
gme.<strong>format_regression_table</strong>(<em>results_dict:dict = None,
                             variable_list:List[str] = [],
                             format:str = 'txt',
                             se_below:bool = True,
                             significance_levels:List[float] = [0.1,0.05,0.10],
                             round_values:int = 3,
                             omit_fe_prefix:List[str] = [],
                             table_columns:list = [],
                             path:str = None,
                             include_index:bool = False,
                             latex_syntax:bool = False,
                             r_squared:bool = False</em>):

## Description
Format estimation results into a standard table format with options for significance stars, LaTeX syntax, standard error positioning, rounding, fixed effect omission, and others options.

## Arguments
<dl>
<dt><strong>results_dict</strong>: <em>Dict[statsmodels.genmod.generalized_linear_model.GLMResultsWrapper]</em> </dt>
  <dd><p>A dictionary of GLM fit objects from statsmodels </p></dd>

 <dt><strong>variable_list</strong>: (optional) <em>List[str]</em> </dt>
  <dd><p>A list of variables to include in the results table. If none are provided, all variables are included. The default is an empty list, which results in the inclusion of all estimated variables. </p></dd>     

<dt><strong>format</strong>: <em>str</em> </dt>
  <dd><p>Determines the file formatting of text. Accepts 'tex' for LaTeX, 'txt' for plain text, or 'csv' for a csv table. Default is 'txt'. </p></dd>

<dt><strong>se_below</strong>: <em>bool</em> </dt>
  <dd><p>If True, standard errors are presented below estimates. If False, they are presented in a column to the right. The default is True. </p></dd>

<dt><strong>significance_levels</strong>: <em>List[float]</em> </dt>
  <dd><p>A list specifying the three percentages, from lowest to highest, on which to base significance stars. The default value is [0.01, 0.05, 0.10]. </p></dd>

<dt><strong>round_values</strong>: <em>int</em> </dt>
  <dd><p>The number of decimal points to include in the reported figures. The default is 3.</p></dd> 

<dt><strong>omit_fe_prefix</strong>: (optional) <em>List[str]</em> </dt>
  <dd><p>A list of strings such that any variable starting with that string are omitted from the created table. The value is an empty list that omits no variables.</p></dd>

<dt><strong>table_columns</strong>: (optional) <em>List[str]</em> </dt>
  <dd><p>A list of keys from the results_dict to be included in the created table. The default is an empty list, which results in all values being created </p></dd>

<dt><strong>path</strong>: (optional) <em>str</em> </dt>
 <dd><p> A system path and file name to write the created table to.  File extensions of .txt (format = 'txt'), .tex or .txt (format = 'tex'), or .csv (format = 'csv') are recommended. </p></dd>

<dt><strong>include_index</strong>: <em>bool/<em> </dt>
  <dd><p>If true, the outputed .csv file will contain row numbers. Default is False. </p></dd>

<dt><strong>latex_syntax</strong>: <em>bool</em> </dt>
  <dd><p>If true, the table will include LaTeX syntax, regardless of the chosen format. Default is False. </p></dd>

<dt><strong>variable_order</strong>: (optional) <em>List[str]</em> </dt>
  <dd><p>If supplied, provides an specific ordering in which to list the variables in the table.</p></dd>

<dt><strong>r_squared</strong>:  <em>bool</em> </dt>
  <dd><p>If True, it includes R^2 values in the table. This is primarily useful if OLS regression results are supplied. Default is False. </p></dd>
 
 <dt><strong>note</strong>: <em>(optional) str</em></dt>
  <dd><p>Adds an optional note to the bottom of a table written via the <em>path</em> argument.</p></dd>

</dl>

## Returns
<strong>Returns:</strong> <em>Pandas.DataFrame</em> 
  A DataFrame containing the formatted results table with specified syntax. 

## Examples
```python

# Create a .csv file.
>>> sample_estimation_model.format_regression_table(format = 'csv',
                                                    path = "c:\folder\saved_results.csv")

# Create a LaTeX .tex table without fixed effects (with prefix 'imp_fe_' and 'exp_fe_')
>>> sample_estimation_model.format_regression_table(format = 'tex',
...                                                 path = "c:\folder\saved_results.tex",
...                                                 omit_fe_prefix = ['imp_fe_' , 'exp_fe_'],
...                                                 note = 'Estimation run on July 7, 2020 by Peter Herman.')
```