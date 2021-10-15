## Data Summary
**[tablulate_by_group(tab_variables,by_group,how)](../api_docs/EstimationData/#methods)** Summarize columns by a user-specified grouping. Can be used to tabulate, aggregate, and summarize data.

**[year_list](../api_docs/EstimationData/#methods)**: Returns a list of years present in the data.

**[countries_each_year](../api_docs/EstimationData/#methods)**: Returns a dictionary keyed by year ID containing a list of country IDs present in each corresponding year.

**[sector_list](../api_docs/EstimationData/#methods)**: Returns a list of unique sector IDs.

**[dtypes](../api_docs/EstimationData/#methods)**: Returns the data types of the columns in the EstimationData.data_frame using Pandas.DataFrame.dtypes(). See [Pandas documentation](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.dtypes.html#pandas.DataFrame.dtypes) for more information.

**[info](../api_docs/EstimationData/#methods)**: Print summary information about EstimationData.data_frame using Pandas.DataFrame.info(). See [Pandas documentation](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.info.html#pandas.DataFrame.info) for more information.

**[describe](../api_docs/EstimationData/#methods)**: Generates some descriptive statistics for EstimationData.data_frame using Pandas.DataFrame.describe(). See [Pandas documentation](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.describe.html#pandas.DataFrame.describe) for more information.

**[add_note(note)](../api_docs/EstimationData/#methods)**: Add a note to the list of notes in 'notes' attribute.
    
## Estimation
**[estimate](../api_docs/EstimationModel/#methods)**: Estimate a PPML model

**[combine_sector_results](../api_docs/EstimationModel/#methods)**: Combine multiple result_dict entries into a single data frame.

**[format_regression_table](../api_docs/EstimationModel/#methods)**: Format regression results into a text, csv, or LaTeX table for presentation.

