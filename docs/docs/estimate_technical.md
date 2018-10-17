<script type="text/x-mathjax-config">
MathJax.Hub.Config({
  TeX: { equationNumbers: { autoNumber: "AMS" } }
});
</script>
<script src='https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.4/latest.js?config=TeX-MML-AM_CHTML' async></script>

# Gravity Estimation Methodology

## Theory-based gravity equation

The GME module estimates the [structural gravity equation](https://www.wto.org/english/res_e/publications_e/advancedguide2016_e.htm) \eqref{eq:gravity} using the Poisson Pseudo Maximum Likelihood (PPML) estimator, a special case of the the Generalized Linear Model (GLM) framework.

\begin{equation}
    X_{ij} =\frac{Y_i E_j}{Y}\left(\frac{t_{ij}}{S_i P_j}\right)^{1-\sigma}.
    \label{eq:gravity}
\end{equation}

In this equation, $X_{ij}$ are the value of exports from country $i$ to country $j$, $Y_{i}$ is country $i$'s domestic production, $E_{j}$ is country $j$'s aggregate expenditure, $Y$ is global production, $t_{ij}$ is the bilateral cost of trading between country $i$ and country $j$, and $\sigma\$ is the elasticity of substitution among goods from varying source countries. The structural terms $S_{i}$ and $P_{j}$ represent multilateral resistance within the exporting and importing countries (i.e the ease of market access for country $i$'s export, and the ease of market access for country $j$'s imports, respectively). 

When applying equation \eqref{eq:gravity} to data using PPML, a variety of fixed effects are possible. One theory-consistent and flexible empirical form of the gravity equation when using panel data is

\begin{equation}
    X_{ijt} =\exp \left[\gamma_{it}+\eta_{jt}+\lambda_{ij}+\beta Z_{ijt}\right]+\varepsilon_{ijt}
    \label{eq:PPML_gravity_panel}
\end{equation}

In equation \eqref{eq:PPML_gravity_panel}, $\gamma_{it}$ are exporter time-varying fixed effect, $\eta_{jt}$ are importer time-varying fixed effects, $\lambda_{ij}$ are exporter-importer time-invariant fixed effects, and $Z_{ijt}$ is the vector of time-variant bilateral determinants of trade, such as tariff levels.

If only cross-section data is available, a theory-consistent empirical form of the gravity equation could be

\begin{equation}
    X_{ij} =\exp \left[\gamma_{i}+\eta_{j}+\beta Z_{ij}\right]+\varepsilon_{ij}
    \label{eq:PPML_gravity_cross}
\end{equation}

In this case, $\gamma_{it}$ are exporter fixed effect, $\eta_{jt}$ are importer fixed effects, and $Z_{ij}$ is the vector of bilateral determinants of trade, such as distance.

## Estimation Procedure

The method ***estimate*** performs a sector-by-sector GLM estimation based on a Poisson distribution with data diagnostics that help increase the likelihood of convergence. See [estimate](api_docs/estimate_method.md).  If sector_by_sector is specified, the routine is repeated for each sector individually, estimating a separate model each time. The estimate routine inherits all specifications from those supplied to the *EstimationModel*.

## Technical Details of PPML Implementation

We implement PPML following [Santos Silva and Tenreyro (2006)](https://www.mitpressjournals.org/doi/pdf/10.1162/rest.88.4.641). The PPML assumes that the variance is proportional to the mean so that the only condition required for PPML to be consistent is the correct specification of the conditional mean. The PPML also gives the same weight to each observation in the estimation and so is desirable when there is not much available information on the nature of heteroscedasticity in the trade data. [Santos Silva and Tenreyro (2006)](https://www.mitpressjournals.org/doi/pdf/10.1162/rest.88.4.641) provide simulation evidence that the PPML is well behaved in a wide range of situations and can deal with certain types of measurement error in the dependent variable. The PPML, being a non-linear estimator, is also able to handle zero trade flows in the estimation.

Common problems with PPML estimation include the non-existence of estimates due to perfect collinearity and numerical difficulties in running the algorithm.

### Non-existence of estimates

[Santos Silva and Tenreyro (2010)](https://www.sciencedirect.com/science/article/pii/S0165176510000832?via%3Dihub) show that PPML estimates may not exist if there is perfect collinearity for the subsample with positive observations of the dependent variable (common in trade data where some countries do not trade in certain years or sectors and so are perfectly collinear when $X_{ij}>0$). In this scenario, either the estimation algorithm will fail to converge or convergence is spurious and characterized by a “perfect” fit for observations where $X_{ij}=0$. To check for non-existence, [Santos Silva and Tenreyro (2011)](https://www.stata-journal.com/article.html?article=st0225) use a short STATA code that first identifies and drops the problematic regressors before estimating it with PPML. Their code also issues a warning that the model is overfitting due to spurious convergence. We implement their STATA code in Python in order to obtain the same procedures for identifying and dropping problematic variables, testing for perfect collinearity and checking if the $X_{ij}=0$ observations are perfectly predicted by the estimated model. All these diagnostics are stored as PPML diagnostics and available to the user after every GME estimation.

### Non-convergence

[Santos Silva and Tenreyro (2011)](https://www.stata-journal.com/article.html?article=st0225) also find that sensitivity to numerical problems can prevent estimation algorithms from locating the maximum and finding PPML estimates that converge. In particular, these numerical issues arise when there are collinear regressors that have different magnitudes or regressors that are extremely, but not perfectly collinear. They recommend using the iterated, re-weighted least squares (IRLS) as the optimization algorithm to deal with such numerical complications, which is also the default method for GLM estimation in the [statsmodels](https://www.statsmodels.org) package used by GME. Thus, the PPML estimator in GME is robust to numerical problems arising from different data configurations.
