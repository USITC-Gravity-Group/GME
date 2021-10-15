# Version 1.3 Updates
Several updates have been made to address bugs, improve the robustness of the estimation procedure, and add features. The only change that affects backward compatibility with version 1.2 is the change to the omit_fixed_effect argument, which now takes a different form.

## Bug Fixes
 *  Fixed error in format_regression_table in which the default significance levels were 0.1, 0.05, and 0.1 rather than 0.01, 0.05, and 0.1. The error was causing estimates to receive *** when they were only 10% significant. [Peter Herman]
 
 * Fixed issue with the retention of record identifiers in EstimationModel.modified_data after estimation. Previously, the modified estimation data did not include identifiers like importer, exporter, or year. These identifiers are now included in the modified data. [Saad Ahmad]

## Improved Robustness
* The omit_fixed_effect argument has been made more robust. It now allows for users to select specific fixed effects to drop in order to avoid collinearity. Notably, the new implementation uses dictionary inputs instead of list inputs so that older uses will no longer work properly in version 1.3. [Saad Ahmad]

* The estimation procedure is now better able to account for cases when there are only non-zero trade flows in the dataset. [Saad Ahmad]

## New Features
* Option for clustered standard errors has been added to gme.EstimationModel.estimate() [Saad Ahmad]

* Added method for creating 'pair' variables in EstimationData [Saad Ahmad]

* Aug 13, 2019: Added make_data_square function [Peter Herman]

* Oct 26, 2018: Added *correlation()* method to *EstimationData*, which produces a correlation table and visualization. [Peter Herman]

* July 7, 2019: Added kernel density plot function *coefficient_kd_plot()* to *EstimationModel* for sector-by-sector estimated results. [Peter Herman]

* Tables created by format_regression_table now report the significance levels at the bottom of the table when written to a file. There is now also an optional *notes* argument to add a user-supplied note to the bottom of the written table. [Peter Herman]











