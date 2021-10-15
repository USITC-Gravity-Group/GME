## Function
<strong>combine_sector_results</strong>(<em>result_dict:dict = None,
                            write_path:str = None,
                            significance_stars: bool = False,
                            round_results: int = None,
                            latex_syntax: bool = True</em>)
                            
## Description
Extract key result fields (coefficients, standard errors, and p-values) and combine them in a DataFrame. Has the option to write the data to a .csv file with or without extra value formatting options.

## Arguments
<dl>
<dt><strong>result_dict</strong>: <em>Dict[statsmodels.genmod.generalized_linear_model.GLMResultsWrapper]</em> </dt>
  <dd><p>A dictionary of GLM fit objects as returned by gme.EsimationModel.estimate()</p></dd>

<dt><strong>write_path</strong>: (optional) <em>str</em> </dt>
  <dd><p>A system location and file name in which to write a csv file containing the combined results. </p></dd>

<dt><strong>significance_stars</strong>: <em>bool</em> </dt>
  <dd><p>If true, combined results are output with significance stars. \*\*\*&#60;0.01, \*\*&#60;0.05, and \*&#60;0.10. Default is False.</p></dd>

<dt><strong>round_results</strong>: (optional) <em>int</em> </dt>
  <dd><p>Rounds combined results to the desired decimal place.</p></dd>
        
<dt><strong>latex_syntax</strong>: <em>bool</em> </dt>
  <dd><p>If True, reports aspects of results, such as significance stars, using standard latex syntax.</p></dd>
</dl>
## Returns
<strong>Returns</strong>: <em>Pandas.DataFrame</em> 
  A DataFrame containing combined GLM results for all results in the supplied dictionary.

## Examples
```python
# Using a gme.EstimationModel named 'sample_model'.
>>> sample_results = sample_model.estimate()

# Return a dataframe of results
>>> result_df = combine_sector_results(sample_results)
>>> result_df.head(5)
                          all_coeff     all_pvalue   all_stderr
log_distance              -0.739840  9.318804e-211     0.023879
agree_pta                  0.334219   5.134355e-15     0.042719
common_language            0.128770   1.076932e-03     0.039383
contiguity                 0.255161   5.857612e-08     0.047050
importer_year_fe_ARG2013  26.980367   0.000000e+00     0.361228

# Export table as a .csv file
>>> combine_sector_results(sample_results,
...                        round_results = 3, 
...                        path = 'c:\\Documents\\combined_results_saved.csv')
```