## Class
**SlimResults**(*glm_results=None*)

## Description
Create a version of the dictionary of results objects that uses less memory. This is the format of results dictionaries generated under the default options in EstimationModel (i.e. the following argument is executed: *EstimationModel(..., full_results=False)*). The SlimResults object is a smaller subset of the GLMResultsWrapper object in the statsmodels package(for more info, see [statsmodels' GLMResults](https://www.statsmodels.org/0.6.1/generated/statsmodels.genmod.generalized_linear_model.GLMResults.html)). Large attributes, such as copies of the estimating data, are removed from the results to cut back on memory size.  The results most commonly referenced are retained, though.

The SlimResults object retains only the attributes listed below. For additional information see the documentation for the GLMResultsWrapper in the statsmodels package.
## Arguments
**glm_results**: *statsmodels.genmod.generalized_linear_model.GLMResultsWrapper* <br>
&emsp; An instance of the statsmodels.GLM.fit() results object 

## Atributes
**params**: *Pandas Series* <br>
 &emsp; Estimated parameter values 

**aic**: *float* <br>
 &emsp; Akaike Information Criterion 

**bic**: *float* <br>
 &emsp; Bayes Information Criterion 

**llf**: *float* <br>
 &emsp; Value of log-likelihood function 

**nobs**: *float* <br>
 &emsp; number of observations 

**bse**: *Pandas Series* <br>
 &emsp; Beta standard errors for parameter estimates 

**pvalues**: *Pandas Series* <br>
 &emsp; Two-tailed pvalues for parameter estimates 

**family_name**: *str* <br>
 &emsp; Name of distribution family used 

**family_link**: *str* <br>
 &emsp; Estimation link function 

**method**: *str* <br>
 &emsp; Estimation method 

**fit_history**: *int* <br>
 &emsp; Number of iterations completed 

**scale**: *float* <br>
 &emsp; The estimate of the scale / dispersion for the model fit 

**deviance**: *float*<br>
 &emsp; Deviance measure 

**pearson_chi2**: *Pandas Series* <br>
 &emsp; Chi-squared statistic 

**cov_type**: *str*<br>
 &emsp; Covariance type 

**yname**: *str*<br>
 &emsp; Column name of endogenous variable 

**xname**: *List[str]*<br>
 &emsp; Column names of exogenous variables 

**model**: *str*<br>
 &emsp; Model used for fit 

**df_resid**: *float*

**df_model**: *float*

**tvalues**: *Pandas Series* <br>
&emsp; T statistics

**fittedvalues**: *Pandas Series* <br>
&emsp; Linear predicted values 

## Methods
The SlimResults object replicates two methods from the original GLMResultsWrapper object from statsmodels.

**conf_int**: *array*
<dd> create confidence intervals for parameter estimates. 
**Arguments**: <br>

&emsp; **alpha**: (optional) *float* <br>
&emsp;&emsp; The significance level for the confidence interval. <br>
&emsp;&emsp; I.e., The default `alpha` = .05 returns a 95% confidence interval.
            
&emsp; **cols**: (optional) *array-like* <br> 
&emsp;&emsp; `cols` specifies which confidence intervals to return
</dd>


**summary**: *object* <br>
&emsp; print a table summarizing estimation results (replicates statsmodels summary method 
&emsp; for GLM). 
