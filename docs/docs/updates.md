# Version 1.3 Updates
Several updates have been made to address bugs, improve the robustness of the estimation procedure, and add features.
 
???+ tip "Backward Compatibility Issues" 
    Version 1.3 introduces a change that impacts compatibility with version 1.2. There has been a change to the format of *omit_fixed_effect* argument of *EstimationModel* such that past usage will generally not be compatible in version 1.3. See the  *[EstimationModel](../api_docs/EstimationModel)* documentation for details on the new format.


## Bug Fixes
*  Fixed error in format_regression_table in which the default significance levels were 0.1, 0.05, and 0.1 rather than 0.01, 0.05, and 0.1. The error was causing estimates to receive *** when they were only 10% significant. 
 
* Fixed issue with the retention of record identifiers in EstimationModel.modified_data after estimation. Previously, the modified estimation data did not include identifiers like importer, exporter, or year. These identifiers are now included in the modified data returned after estimation. 

* Fixed issue in which pre-estimation diagnostics would drop observations associated with collinear fixed effects if the trade values of those observations were all greater than zero.


## Improved Robustness
* The [omit_fixed_effect](../api_docs/EstimationModel/#arguments) argument has been made more robust. It now allows for users to select specific fixed effects to drop in order to avoid collinearity. Notably, the new implementation uses dictionary inputs instead of list inputs so that older uses will no longer work properly in version 1.3. See 

 

## New Features
* Option for clustered standard errors (*[cluster_on](../api_docs/EstimationModel/#arguments)*) has been added to *EstimationModel*. 

* Added method for creating concatenated 'pair' variables from categorical variables to EstimationData (*[add_pair_var](../api_docs/EstimationData/#methods)*).

* Added *[make_data_square](../api_docs/make_data_square)* function. 

* Added *[correlation](../api_docs/EstimationData/#methods)* method to *EstimationData*, which produces a correlation table and visualization. 

* Added kernel density plot function *[coefficient_kd_plot](../api_docs/coefficient_kd_plot)* to visualize sector-by-sector estimated results. 

* Tables created by format_regression_table now report the significance levels at the bottom of the table when written to a file. There is now also an optional *[notes](../api_docs/format_regression_table/#arguments)* argument to add a user-supplied note to the bottom of the written table. 