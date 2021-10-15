## Function
gme.<strong>coefficient_kd_plot</strong>(<em>estimation_model: EstimationModel,
                        variables: List[str],
                        path: str = None,
                        bandwidth: float = 0.5,
                        rename_variables: dict = None</em>):
                        
## Description
Produce kernel density plots of parameter estimates across different sectors in the results dictionary.

## Arguments
<dl>
<dt><strong>estimation_model</strong>: <em>gme.EstimationModel</em></dt>
 <dd><p>An estimated EstimationModel with more than one sector.</p></dd>

<dt><strong>variables</strong>: <em>List[str]</em></dt>
 <dd><p>A list of model covariates for which to plot kernel densities.</p></dd>

<dt><strong>path</strong>: <em>(optional) str</em></dt>
 <dd><p>A path and file name at which to save the plot. Can end in the following file types for example: pdf, svg, and png.</p></dd>

<dt><strong>bandwidth</strong>: <em>float</em></dt>
 <dd><p>Specify the bandwidth for the density plots. The default is 0.5.</p></dd>

<dt><strong>rename_variables</strong>: <em>(optional)</em></dt>
 <dd><p>A dictionary of alternative variable names to use in the plot. For example {'original_name':'new_name'}</p></dd>

</dl>
## Return
<em>None</em>, plots a figure and, if specified, writes it to a file.

## Examples
```python
>>> est_model = EstimationModel(est_data, lhs_var='trade_value',
                               rhs_var=['contiguity', 'agree_pta', 'border', 'colony', 'ln_dist'],
                               fixed_effects=[['importer', 'year'], ['exporter', 'year']],
                               sector_by_sector=True)
>>> est_model.estimate()
>>> coefficient_kd_plot(est_model, variables = ['contiguity', 'agree_pta', 'border', 'colony', 'ln_dist'],
                        rename_variables = {'agree_pta':'PTA', 'ln_dist':'distance'},
                        path = 'C:\kd_plot.eps')
```