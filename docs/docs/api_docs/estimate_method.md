## Function
**estimate**()

## Description

The method ***estimate*** performs a sector-by-sector GLM estimation based on a Poisson distribution with data diagnostics that help increase the likelihood of convergence. If sector_by_sector is specified, the routine is repeated for each sector individually, estimating a separate model each time. The estimate routine inherits all specifications from those supplied to the *EstimationModel*. The routine follows several steps.

1. **Creates Fixed effects**: Fixed effects are created based on the EstimationModel specification.

2. **Pre-Diagnostics**: Several steps are taken to increase the likelihood that the estimation will converge
    successfully. [Click here to technical details.](/estimate_technical/#non-existence-of-estimates)
    + Perfect Colinearity: Columns and observations that are perfectly collinear are identified and
        excluded.
    + Insufficient Variation: Variables in which there is an insufficient level of
        variation for estimation are excluded. These are typically cases in which a country does not import or export at all for a given level of fixed effect.

3. **Estimate**: Estimation is run using GLM.fit in statsmodels for the Poisson family distribution. Robust standard errors are computed using the HC1 version of the Huber-White estimator for heteroscedasticity consistent covariance matrix.

4. **Post-Diagnostics**: A test for over-fit values as in [Santos Silva and Tenreyro (2011)](http://www.sciencedirect.com/science/article/pii/S0165176511001741).

5. **Results**: The method returns **EstimationModel.results_dict** and stores two others (**EstimationModel.ppml_diagnostics** and **EstimationModel.modified_data**) as attributes of the *EstimationModel*. 

    1. **EstimationModel.results_dict**:  This is a dictionary of results objects from the statsmodels GLM.fit routine, each keyed using either the name of the sector if the estimation was sector-by-sector (i.e. *sector_by_sector = True*) or with the key 'all' if not. It is both returned and stored as **EstimationModel.results_dict**.[^statsmodels_results]
    
    2. **EstimationModel.ppml_diagnostics**: A data frame containing a column of pre- and post-diagnostic information for each regression
    
    3. **EstimationModel.modified_data**: A dictionary using the same keys as results_dict, each containing the modified DataFrames created during the pre-diagnostic stages of the estimations. Because of the large memory footprint of this assignment, storing it is optional and only done if specified (i.e. *EstimationModel.retain_modified_data = True*)
    
[^statsmodels_results]: For more details about the *statsmodels* results object, see [http://www.statsmodels.org/0.6.1/generated/statsmodels.genmod.generalized_linear_model.GLMResults.html](http://www.statsmodels.org/0.6.1/generated/statsmodels.genmod.generalized_linear_model.GLMResults.html).

### Example
```python
# Create fixed effects and specify sector by sector estimation
>>> gme_data = gme.EstimationData(data_frame = sample_data,
                              imp_var_name = 'importer',
                              exp_var_name = 'exporter',
                              sector_var_name = 'sector'
                              trade_var_name = 'trade_value',
                              year_var_name = 'year')
                              
>>> sample_estimation_model = gme.EstimationModel(estimation_data = gme_data, 
                                                lhs_var = 'trade_value', 
                                                rhs_var = ['log_distance','agree_pta','common_language','contiguity'], 
                                                fixed_effects = ['importer', 'exporter'], 
                                                keep_years = [2013, 2014, 2015],
                                                sector_by_sector = True)

# Estimate the model
>>> sample_estimation_model.estimate()

# Generate post-diagnostics
>>> diag = sample_estimation_model.ppml_diagnostics
>>> print(diag)
Overfit Warning                                                                 No
Collinearities                                                                  No
Number of Columns Excluded                                                       3
Perfectly Collinear Variables                                                   []
Zero Trade Variables             [importer_fe_IRN, importer_fe_LBY, importer_fe...

# Extract the results to a new data frame and save to a .csv
>>> results_dictionary = sample_estimation_model.results_dict("c:\folder\saved_results.csv")

```

