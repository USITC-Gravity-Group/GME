__Author__ = "Grace Kenneally, Saad Ahmad"
__Project__ = "gme.estimate"
__Created__ = "08-01-2018"

from scipy import stats
import numpy as np
from statsmodels.compat.python import lzip
import pickle


'''
#Load dictionary of estimation results using pickle
zestimates = pickle.load(open(("G:\\data\\Gravity Resources\\Data\\Africa Data\\Estimation\\results\\zest.pickle"), "rb" ) )
'''

class SlimResults(object):
    def __init__(self, glm_results=None):
        '''
        Create a version of the dictionary of results objects that uses less memory. The SlimResults object is a
        smaller subset of the GLMResultsWrapper object in the statsmodels package. Large attributes, such as
        copies of the estimating data, are removed from the results to cut back on memory size.  The results most
        commonly referenced are retained, though.

        The SlimResults object retains only the attributes listed below. For additional information see the
        documentation for the GLMResultsWrapper in the statsmodels package.

        Args:
            glm_results: statsmodels.genmod.generalized_linear_model.GLMResultsWrapper
                An instance of the satasmodels.GLM.fit() results object.

        Attributes:
            params: Pandas Series
                Estimated parameter values
            aic: float
                Akaike Information Criterion
            bic: float
                Bayes Information Criterion
            llf: float
                Value of log-likelihood function
            nobs: float
                number of observations
            bse: Pandas Series
                Beta standard errors for parameter estimates
            pvalues: Pandas Series
                Two-tailed pvalues for parameter estimates
            family_name: str
                Name of distribution family used
            family_link: str
                Estimation link function
            method: str
                Estimation method
            fit_history: int
                Number of iterations completed
            scale: float
                The estimate of the scale / dispersion for the model fit
            deviance: float
                Deviance measure
            pearson_chi2: Pandas Series
                Chi-squared statistic
            cov_type: str
                Covariance type
            yname: str
                Column name of endogenous variable
            xname: List[str]
                Column names of exogenous variables
            model: str
                Model used for fit
            df_resid: float
            df_model: float
            tvalues: Pandas Series
                T statistics
            fittedvalues: Pandas Series
                Linear predicted values

        Methods:
            The SlimResults object replicates two methods from the original GLMResultsWrapper object from statsmodels.

            conf_int: array
                create confidence intervals for parameter estimates.
            summary: object
                print a table summarizing estimation results (replicates statsmodels summary method fo GLM).

        Returns: object
            A SlimResults object.
        '''
        self.params = glm_results.params
        self.aic = glm_results.aic
        self.bic = glm_results.bic
        self.llf = glm_results.llf
        self.nobs = glm_results.nobs
        self.bse = glm_results.bse
        self.pvalues = glm_results.pvalues
        self.family_name=glm_results.family.__class__.__name__
        self.family_link=glm_results.family.link.__class__.__name__
        self.method=glm_results.method
        self.fit_history=glm_results.fit_history['iteration']
        self.scale=glm_results.scale
        self.deviance=glm_results.deviance
        self.pearson_chi2=glm_results.pearson_chi2
        self.cov_type=glm_results.cov_type
        self.yname=glm_results.model.endog_names
        self.xname=glm_results.model.exog_names
        self.model=glm_results.model.__class__.__name__
        self.df_resid=glm_results.df_resid
        self.df_model=glm_results.df_model
        self.tvalues=glm_results.tvalues
        self.fittedvalues = glm_results.fittedvalues
       

    
    def conf_int(self, alpha=.05, cols=None, method='default'):
            """
            Returns the confidence interval of the fitted parameters.

            Parameters
            ----------
            alpha : float, optional
                The significance level for the confidence interval.
                ie., The default `alpha` = .05 returns a 95% confidence interval.
            cols : array-like, optional
                `cols` specifies which confidence intervals to return
            method : string
                Not Implemented Yet
                Method to estimate the confidence_interval.
                "Default" : uses self.bse which is based on inverse Hessian for MLE
                "hjjh" :
                "jac" :
                "boot-bse"
                "boot_quant"
                "profile"


            Returns
            --------
            conf_int : array
                Each row contains [lower, upper] limits of the confidence interval
                for the corresponding parameter. The first column contains all
                lower, the second column contains all upper limits.

            Examples
            --------
            >>> import statsmodels.api as sm
            >>> data = sm.datasets.longley.load()
            >>> data.exog = sm.add_constant(data.exog)
            >>> results = sm.OLS(data.endog, data.exog).fit()
            >>> results.conf_int()
            array([[-5496529.48322745, -1467987.78596704],
                   [    -177.02903529,      207.15277984],
                   [      -0.1115811 ,        0.03994274],
                   [      -3.12506664,       -0.91539297],
                   [      -1.5179487 ,       -0.54850503],
                   [      -0.56251721,        0.460309  ],
                   [     798.7875153 ,     2859.51541392]])


            >>> results.conf_int(cols=(2,3))
            array([[-0.1115811 ,  0.03994274],
                   [-3.12506664, -0.91539297]])

            Notes
            -----
            The confidence interval is based on the standard normal distribution.
            Models wish to use a different distribution should overwrite this
            method.
            """
            bse = self.bse
    
            dist = stats.t
            df_resid = getattr(self, 'df_resid_inference', self.df_resid)
            q = dist.ppf(1 - alpha / 2, df_resid)
    
            if cols is None:
                lower = self.params - q * bse
                upper = self.params + q * bse
            else:
                cols = np.asarray(cols)
                lower = self.params[cols] - q * bse[cols]
                upper = self.params[cols] + q * bse[cols]
            return np.asarray(lzip(lower, upper))
   
    def summary(self, yname=None, xname=None, title=None, alpha=.05):
        """
        Summarize the Regression Results

        Parameters
        -----------
        yname : string, optional
            Default is `y`
        xname : list of strings, optional
            Default is `var_##` for ## in p the number of regressors
        title : string, optional
            Title for the top table. If not None, then this replaces the
            default title
        alpha : float
            significance level for the confidence intervals

        Returns
        -------
        smry : Summary instance
            this holds the summary tables and text, which can be printed or
            converted to various output formats.

        See Also
        --------
        statsmodels.iolib.summary.Summary : class to hold summary
            results

        """

        top_left = [('Dep. Variable:', None),
                    ('Model:', [self.model]),
                    ('Model Family:', [self.family_name]),
                    ('Link Function:', [self.family_link]),
                    ('Method:', [self.method]),
                    ('Covariance Type:', [self.cov_type]),
                    ('No. Observations:', [self.nobs])
                    ]

        top_right = [('No. Iterations:',
                     ["%d" % self.fit_history]),
                     ('Df Residuals:', [self.df_resid]),
                     ('Df Model:', [self.df_model]),
                     ('Scale:', ["%#8.5g" % self.scale]),
                     ('Log-Likelihood:', ["%#8.5g" % self.llf]),
                     ('Deviance:', ["%#8.5g" % self.deviance]),
                     ('Pearson chi2:', ["%#6.3g" % self.pearson_chi2])
                     ]

        if title is None:
            title = "Generalized Linear Model Regression Results"

        # create summary tables
        y=self.yname
        x=self.xname

        from statsmodels.iolib.summary import Summary
        
                    
        smry = Summary()
        smry.add_table_2cols(self, gleft=top_left, gright=top_right,  # [],
                             yname=y, xname=x, title=title)
        smry.add_table_params(self, yname=y, xname=x, alpha=0.05,
                              use_t=True)

        if hasattr(self, 'constraints'):
            smry.add_extra_txt(['Model has been estimated subject to linear '
                                'equality constraints.'])

        # diagnostic table is not used yet:
        # smry.add_table_2cols(self, gleft=diagn_left, gright=diagn_right,
        #                   yname=yname, xname=xname,
        #                   title="")

        return smry



