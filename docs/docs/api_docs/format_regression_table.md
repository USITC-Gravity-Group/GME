## Function
gme.**format_regression_table**(*results_dict:dict = None,
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
                             r_squared:bool = False*):

## Description
Format estimation results into a standard table format with options for significance stars, LaTeX syntax, standard error positioning, rounding, fixed effect omission, and others options.

## Arguments
**results_dict**: *Dict[statsmodels.genmod.generalized_linear_model.GLMResultsWrapper]*<br> 
 &emsp; A dictionary of GLM fit objects from statsmodels 

 **variable_list**: (optional) *List[str]*<br> 
 &emsp; A list of variables to include in the results table. If none are provided, all variables are included. <br> 
 &emsp; The default is an empty list, which results in the inclusion of all estimated variables.      

**format**: *str*<br> 
 &emsp; Determines the file formatting of text. Accepts 'tex' for LaTeX, 'txt' for plain text, or 'csv' for a <br> 
 &emsp; csv table. Default is 'txt'. 

**se_below**: *bool*<br> 
 &emsp; If True, standard errors are presented below estimates. If False, they are presented in a <br> 
 &emsp; column to the
right. The default is True. 

**significance_levels**: *List[float]*<br> 
 &emsp; A list specifying the three percentages, from lowest to highest, on which to base significance <br> 
 &emsp; stars. The default value is [0.01, 0.05, 0.10]. 

**round_values**: *int*<br> 
 &emsp; The number of decimal points to include in the reported figures. The default is 3. 

**omit_fe_prefix**: (optional) *List[str]*<br> 
 &emsp; A list of strings such that any variable starting with that string are omitted from the created <br> 
 &emsp; table. The value is an empty list that omits no variables.

**table_columns**: (optional) *List[str]*<br> 
 &emsp; A list of keys from the results_dict to be included in the created table. The default is an empty <br> 
 &emsp; list, which results in all values being created 

**path**: (optional) *str*<br> 
 &emsp; A system path and file name to write the created table to.  File extensions of .txt (format = 'txt'),<br> 
 &emsp; .tex or .txt (format = 'tex'), or .csv (format = 'csv') are recommended. 

**include_index**: *bool*<br> 
 &emsp; If true, the outputed .csv file will contain row numbers. Default is False. 

**latex_syntax**: *bool*<br> 
 &emsp; If true, the table will include LaTeX syntax, regardless of the chosen format. Default is False. 

**variable_order**: (optional) *List[str]*<br> 
 &emsp; If supplied, provides an specific ordering in which to list the variables in the table.

**r_squared**:  *bool*<br> 
 &emsp; If True, it includes R^2 values in the table. This is primarily useful if OLS regression results <br> 
 &emsp; are supplied. Default is False. 

## Returns
**Returns:** *Pandas.DataFrame*<br> 
 &emsp; A DataFrame containing the formatted results table with specified syntax. 

## Examples
```python

# Create a .csv file.
>>> sample_estimation_model.format_regression_table(format = 'csv',
                                                    path = "c:\folder\saved_results.csv")

# Create a LaTeX .tex table without fixed effects (with prefix 'imp_fe_' and 'exp_fe_')
>>> sample_estimation_model.format_regression_table(format = 'tex',
...                                                 path = "c:\folder\saved_results.tex",
...                                                 omit_fe_prefix = ['imp_fe_' , 'exp_fe_'])
```