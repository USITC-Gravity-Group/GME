# Tutorials
The following tutorials are meant to introduce users to the gme package and help them become proficcient with many of the features that it offers.

* **Tutorial 1 - Estimating a Gravity Model**: This example demonstrates a basic gravity analysis including loading data, constructing some summary statistics, estimating a model, and outputing the results in several possible formats.


## Tutorial 1 - Estimating a Gravity Model
### Load Data
The gme package uses a special object to manage data: the gme.EstimationData.  The data can be thought of as a specialized Pandas DataFrame.[^DataFrame]  The EstimationData features a Pandas.DataFrame containing data (trade + gravity + etc.) for estimation as well as additional information about that data and methods that can be used to summarize and/or manipulate the data.  This tutorial will demonstrate some of these features.

First, we must begin by creating a gme.EstimationData.  Doing so requires the inputting of a Pandas.DataFrame and several pieces of "meta-data" that describe the data. Start by loading a dataset using the *read_csv()* function from pandas.  In the sample code below, we will read a dataset directly from the internet, but you could just as easily read the same file from you hard drive. 

```python tab="Code and output"
>>> import gme as gme
>>> import pandas as pd

>>> gravity_data = pd.read_csv('https://www.usitc.gov/data/gravity/example_trade_and_grav_data_small.csv')

>>> gravity_data.head()
  importer exporter  year   trade_value  agree_pta  common_language  \
0      AUS      BRA  1989  3.035469e+08        0.0              1.0   
1      AUS      CAN  1989  8.769946e+08        0.0              1.0   
2      AUS      CHE  1989  4.005245e+08        0.0              1.0   
3      AUS      DEU  1989  2.468977e+09        0.0              0.0   
4      AUS      DNK  1989  1.763072e+08        0.0              1.0 
  
   contiguity  log_distance  
0         0.0      9.553332  
1         0.0      9.637676  
2         0.0      9.687557  
3         0.0      9.675007  
4         0.0      9.657311 
 

# Next, we use the loaded data to create a EstimationData 
>>> gme_data = gme.EstimationData(data_frame=gravity_data,
                              imp_var_name='importer',
                              exp_var_name='exporter',
                              trade_var_name='trade_value',
                              year_var_name='year',
                              notes='Downloaded from https://www.usitc.gov/data/gravity/example_trade_and_grav_data_small.csv')
```
```Python tab="Code only"
import gme as gme
import pandas as pd
gravity_data = pd.read_csv('https://www.usitc.gov/data/gravity/example_trade_and_grav_data_small.csv')
gravity_data.head()
gme_data = gme.EstimationData(data_frame=gravity_data,
                              imp_var_name='importer',
                              exp_var_name='exporter',
                              trade_var_name='trade_value',
                              year_var_name='year',
                              notes='Downloaded from https://www.usitc.gov/data/gravity/example_trade_and_grav_data_small.csv')
```
In creating the EstimationData object, the user is asked to supply a Pandas.DataFrame, which we a loaded in the previous lines, and several types of descriptive arguments. These arguments (*imp_var_name*, *exp_var_name*, *trade_var_name*, and *year_var_name*) specify the columns in the supplied DataFrame corresponding to particular types of information that will likely be present in any gravity analysis (the column containing the importer ID, exporter ID, trade values, and year, respectively). These "meta-data" fields can be useful as they prevent users from having to re-enter these same basic characteristics of the data at later points and permit the automatic construction of certain types of summary information. Finally, an optional *note* is supplied to the EstimationData. The EstimationData object has a attribute that stores a list user-supplied strings for later reference. In this case, we have supplied a note indicating from where the data originated.
  
### Working with the EstimationData
In addition to providing a object class that communicates conveniently with the gme.EstimationModel (see below), the EstimationData provides a collection of data summary and manipulation tools.  For example, simply calling (or printing) the object, returns a summary of the scope of the data:

```python
>>> gme_data
number of countries: 62 
number of exporters: 62 
number of importers: 62 
number of years: 27 
number of sectors: not_applicable 
dimensions: (98612, 8)
```
As can be seen from the console return, the dataset we are using covers 62 importers and exporters, 27 years, and contains 98,612 rows and 8 columns. Because this particular dataset does not have multiple sectors, that field is marked as 'not applicable'.[^sector_var_name] 

Other summary information can be reported in the following ways:
```python
# Return the number of importers in the dataset.
>>> gme_data.number_of_importers
62

# Return a list of the column names
>>> gme_data.columns
['importer', 'exporter', 'year', 'trade_value', 'agree_pta', 'common_language', 
'contiguity', 'log_distance']

# Return a list of years in the dataset
>>> gme_data.year_list() 
[1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 
2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015]

# Return a dictionary containing a list of countries in the dataset for each year.
>>> country_list = gme_data.countries_each_year()
>>> country_list[1989]
['IRN', 'BOL', 'TUR', 'ARG', 'CHL', 'HUN', 'KEN', 'VEN', 'ZAF', 'URY', 'BRA', 'DZA',
 'PER', 'IRL', 'DNK', 'GHA', 'KOR', 'PAK', 'COL', 'IND', 'ISL', 'ISR', 'ESP', 'ITA',
 'NLD', 'NGA', 'AUS', 'SWE', 'PRY', 'GBR', 'IDN', 'HKG', 'NOR', 'TUN', 'EGY', 'KWT', 
 'DEU', 'CHE', 'MYS', 'NZL', 'LBY', 'USA', 'SDN', 'CHN', 'GRC', 'MEX', 'CAN', 'PRT', 
 'SAU', 'POL', 'PHL', 'THA', 'FRA', 'JPN', 'MAR', 'AUT', 'FIN', 'SGP', 'ECU']
 
# Additionally, many of the descriptive methods from Pandas.DataFrames have been inherited:
>>> gme_data.dtypes()
importer            object
exporter            object
year                 int64
trade_value        float64
agree_pta          float64
common_language    float64
contiguity         float64
log_distance       float64
dtype: object

>>> gme_data.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 98612 entries, 0 to 98611
Data columns (total 8 columns):
importer           98612 non-null object
exporter           98612 non-null object
year               98612 non-null int64
trade_value        98612 non-null float64
agree_pta          97676 non-null float64
common_language    97676 non-null float64
contiguity         97676 non-null float64
log_distance       97676 non-null float64
dtypes: float64(5), int64(1), object(2)
memory usage: 6.0+ MB

>>> gme_data.describe()
               year   trade_value     agree_pta  common_language  \
count  98612.000000  9.861200e+04  97676.000000     97676.000000   
mean    2002.210441  1.856316e+09      0.381547         0.380646   
std        7.713050  1.004735e+10      0.485769         0.485548   
min     1989.000000  0.000000e+00      0.000000         0.000000   
25%     1996.000000  1.084703e+06      0.000000         0.000000   
50%     2002.000000  6.597395e+07      0.000000         0.000000   
75%     2009.000000  6.125036e+08      1.000000         1.000000   
max     2015.000000  4.977686e+11      1.000000         1.000000   

         contiguity  log_distance  
count  97676.000000  97676.000000  
mean       0.034051      8.722631  
std        0.181362      0.818818  
min        0.000000      5.061335  
25%        0.000000      8.222970  
50%        0.000000      9.012502  
75%        0.000000      9.303026  
max        1.000000      9.890765  
```

Additionally, the EstimationData object retains the full ability to work with the supplied DataFrame.  The DataFrame can be easily accessed by referring to its attribute in EstimationData.
```python
# Return the column of trade_values
>>> gme_data.data_frame['trade_value']
0        3.035469e+08
1        8.769946e+08
2        4.005245e+08
             ...     
98609    0.000000e+00
98610    0.000000e+00
98611    0.000000e+00
Name: trade_value, Length: 98612, dtype: float64
```

Finally, the EstimationData object features a tool for easy aggregation and custom summary information. Additionally, because the method used for this process returns a DataFrame, the aggregated information can itself be used for many other applications, including the creation of a new EstimationData object.

```python
# Calculate mean, minimum, and maximum trade values and distances for each importer.
>>> aggregated_data_1 = gme_data.tabulate_by_group(tba_variables = ['trade_value',
                                                                    'log_distance'],
                                                   by_group = ['importer'],
                                                   how = ['mean','min','max'])
>>> aggregated_data_1.head(5)
  importer_  trade_value_mean  trade_value_min  trade_value_max  \
0       ARG      4.579184e+08              0.0     2.218091e+10   
1       AUS      1.704595e+09              0.0     4.620843e+10   
2       AUT      1.241109e+09              0.0     6.973252e+10   
3       BEL      4.783322e+09              0.0     9.963373e+10   
4       BOL      5.506187e+07              0.0     1.810665e+09   

   log_distance_mean  log_distance_min  log_distance_max  
0           9.137979          6.377581          9.856877  
1           9.421134          7.926203          9.774024  
2           8.231444          5.723756          9.800177  
3           8.223088          5.061335          9.824095  
4           9.090685          7.150738          9.874070

# Calculate mean, standard deviation, and count of trade for each imoprter/exporter pair.
>>> aggregated_data_2 = gme_data.tabulate_by_group(
                                tab_variables = ['trade_value'],
                                by_group = ['importer','exporter'],
                                how = ['mean','std', 'count'])
>>> aggregated_data_2.head(5)
  importer_ exporter_  trade_value_mean  trade_value_std  trade_value_count
0       ARG       AUS      1.205231e+08     1.056954e+08                 27
1       ARG       AUT      9.942091e+07     8.018963e+07                 27
2       ARG       BEL      2.972734e+08     2.129833e+08                 17
3       ARG       BOL      3.378161e+08     6.339966e+08                 27
4       ARG       BRA      8.209756e+09     6.723047e+09                 27
```
!!! note
    **Knowing when to end a command with *( )*:** When first learning python, it can be confusing trying to determine when a command applied to an object should be followed by parentheses. In the preceding code example, you will see instances of both: *gme_data.columns* and *gme_data.year_list( )*, for example.  Knowing which format to use is largely a matter of becoming familiar with the functions you are using.  However, there is a logic to it.  Each time a command is applied to an object (i.e. using the syntax *object.command*), you are calling either an **attribute** of the object or a **method** on the object.  An attribute is a piece of information that has already been created and included in the object whereas a method is effectively a function that can be run on the object.  A method will be called with two parentheses because they will often accept additional arguments. For example, this is the case with the DataFrame method *head( )*, which can accept a user-provided number of rows.  However, you will often find that you do not need to supply additional arguments to a method, in which case you leave the parentheses empty.  An attribute, by comparison, does not feature *( )* because there is no need or ability to provide additional input because the contents of that attribute have already been computed. As mentioned before, knowing whether a command is an attribute or a method, however, simply requires familiarity with the object.  

### Creating and estimating a model
Once a EstimationData has been created, estimating a gravity model using the data is fairly straight forward.  There are two basic step for estimation.
1. Define a model
2. Estimate the model

Defining the model amounts to creating another object called a *EstimationModel*.  Like the EstimationData, the Estimation model is meant to standardize and simplify the steps typically taken to specify and estimate a gravity model.  While the EstimationData is meant to be an object that is created once for each study, many EstimationModels will likely be defined and redefined as you test different specifications. Thus, the arguments and attributes of the EstimationModel reflect the different types of modifications you may want to make as you select your preferred specification. 

As with the EstimationData, the EstimationModel is largely a dataset---this time in the form of the EstimationData---with added information that define the characteristics of the particular model. The following example depict several model specifications, each demonstrating different types of model aspects that can be specified.

```python
# A simple case in which 'trade_value' is dependent on 'log_distance', 'agree_pta', etc.
>>> model_baseline = gme.EstimationModel(data_object = gme_data,
                                         lhs_var = 'trade_value',
                                         rhs_var = ['log_distance',
                                                    'agree_pta', 
                                                    'common_language',
                                                    'contiguity'])

# A specification that will generate and include importer-year and exporter-year
# fixed effects                                                    
>>> fixed_effects_model  = gme.EstimationModel(data_object = gme_data,
                                 lhs_var = 'trade_value',
                                 rhs_var = ['log_distance',
                                            'agree_pta', 
                                            'common_language',
                                            'contiguity'],
                                 fixed_effects=[['importer','year'],
                                                ['exporter','year']])

# A specification that uses a subset of the data. The United States ('USA') will be omitted
# and only the years 2013--2015 will be included.
>>> data_subset_model = gme.EstimationModel(data_object = gme_data,
                                            lhs_var = 'trade_value',
                                            rhs_var = ['log_distance',
                                                       'agree_pta', 
                                                       'common_language',
                                                       'contiguity'],
                                            drop_imp_exp=['USA'],
                                            keep_years=[2015, 2014, 2013])                                                  
```    
When specifying the model, there are several key types of attributes that can be included.

* **Model Variables**: The variables to be included are specified using the arguments *lhs_vars* and *rhs_vars*, which denote the left-hand-side dependent variable and right-hand-side independent variables, respectively.
* **Fixed Effects**: The model, at the point at which it is estimated, will constructed fixed effects if any are specified by *fixed_effects*.  These can be either single variables (e.g. \['importer'\]), or interacted variables (e.g. \['importer', 'year'\]).
* **Data Subsets**: Subsets of the data to use for estimation can be specified in a variety of ways. The arguments *keep_years* and *drop_years* can be used to select only a subset of years to include. Similarly the *keep_imp*, *keep_exp*, and *keep_imp_exp* arguments, and their corresponding *drop_...* options can do the same for importers and/or exporters. 

Once a model has been defined, running a PPML estimation according to the supplied specification is quite straightforward, it only requires the application of a single method of the EstimationModel: *.estimate()*.  No further inputs are required.

```python
# Define a new, fixed effects model using only a subset of years (to reduce the computation time)
>>> fixed_effects_model_2  = gme.EstimationModel(data_object = gme_data,
                                                 lhs_var = 'trade_value',
                                                 rhs_var = ['log_distance',
                                                            'agree_pta', 
                                                            'common_language',
                                                            'contiguity'],
                                                 fixed_effects=[['importer','year'],
                                                                ['exporter','year']],
                                                 keep_years = [2013,2014,2015])

# Conduct a PPML estimation of the fixed effects model.
estimates = fixed_effects_model_2.estimate()
select specification variables: ['log_distance', 'agree_pta', 'common_language', 'contiguity', 'trade_value', 'importer', 'exporter', 'year'], Observations excluded by user: {'rows': 0, 'columns': 0}
drop_intratrade: no, Observations excluded by user: {'rows': 0, 'columns': 0}
drop_imp: none, Observations excluded by user: {'rows': 0, 'columns': 0}
drop_exp: none, Observations excluded by user: {'rows': 0, 'columns': 0}
keep_imp: all available, Observations excluded by user: {'rows': 0, 'columns': 0}
keep_exp: all available, Observations excluded by user: {'rows': 0, 'columns': 0}
drop_years: none, Observations excluded by user: {'rows': 0, 'columns': 0}
keep_years: [2013, 2014, 2015], Observations excluded by user: {'rows': 87632, 'columns': 0}
drop_missing: yes, Observations excluded by user: {'rows': 0, 'columns': 0}
Estimation began at 08:58 AM  on Jun 19, 2018
Estimation completed at 08:58 AM  on Jun 19, 2018

```
 The results (*estimates*) are stored as a dictionary with each entry in the dictionary corresponding to a single estimation.[^results_dict]  The storing of the results in this way is primarily to facilitate the *sector_by_sector*, which separately estimates a model for each product/industry/sector, and returns a set of estimation results for each.  In the case in which multiple sectors are not considered, as in the examples considered here, the results dictionary contains a single entry with the key 'all'.  


### Viewing, formatting, and outputting the results
The first step to viewing and working with the regression estimates is unpacking them from the dictionary in which they have been stored. A dictionary is an object in which each item stored in the dictionary is associated with a key.  That key can be used to return its associated item. In the above example, *estimates* is a dictionary in which each item is an object of results. In this tutorial, there is only one object in this case because only one regression was run. In cases in which multiple regressions are run because multiple sectors are estimated separately, the dictionary would contain multiple results, each keyed with the name of the respective sector. 
```python
# Return a list of keys in the object
>>> estimates.keys()
dict_keys(['all'])

# Return the result object and save it to a new variable for convenience 
>>> results = estimates['all']
``` 

The estimation uses tools from the *statsmodels* package so that the results inherit all of the features of the *statsmodels* GLM results object.[^statsmodels]  This means that the object contains a plethora of fields reflecting things like coefficient estimates, standard errors, p-values, AIC/BIC, etc.  Similarly, there is a useful method associated with the object that can be used for creating summary tables.

```python
# print a summary of the results
>>> results.summary()
<class 'statsmodels.iolib.summary.Summary'>
                 Generalized Linear Model Regression Results                  
==============================================================================
Dep. Variable:            trade_value   No. Observations:                 8700
Model:                            GLM   Df Residuals:                     8371
Model Family:                 Poisson   Df Model:                          328
Link Function:                    log   Scale:                             1.0
Method:                          IRLS   Log-Likelihood:            -4.8282e+12
Date:                Wed, 20 Jun 2018   Deviance:                   9.6565e+12
Time:                        13:36:10   Pearson chi2:                 1.22e+13
No. Iterations:                    10                                         
============================================================================================
                               coef    std err          z      P>|z|      [0.025      0.975]
--------------------------------------------------------------------------------------------
log_distance                -0.7398      0.024    -30.982      0.000      -0.787      -0.693
agree_pta                    0.3342      0.043      7.824      0.000       0.250       0.418
common_language              0.1288      0.039      3.270      0.001       0.052       0.206
contiguity                   0.2552      0.047      5.423      0.000       0.163       0.347
importer_year_fe_ARG2013    26.9804      0.361     74.690      0.000      26.272      27.688
importer_year_fe_ARG2014    26.8032      0.344     77.840      0.000      26.128      27.478
importer_year_fe_AUS2013    28.1690      0.315     89.455      0.000      27.552      28.786
... (truncated for this tutorial)
============================================================================================


# Extract the estimated parameter values (returned as a Pandas.Series)
>>> coefficients = results.params
>>> coefficients,head()
log_distance                -0.739840
agree_pta                    0.334219
common_language              0.128770
contiguity                   0.255161
importer_year_fe_ARG2013    26.980367
dtype: float64

# Extract the standard errors
>>> results.bse
log_distance                0.023879
agree_pta                   0.042720
                              ...   
exporter_year_fe_VEN2015    0.346733
Length: 329, dtype: float64

# Extract the p-values
>>> results.pvalues
log_distance                9.318804e-211
agree_pta                    5.134355e-15
                                ...      
exporter_year_fe_VEN2015     5.681631e-03
Length: 329, dtype: float64                                

# Return fitted values
>>> results.fittedvalues
0       1.610136e+09
1       3.044133e+08
2       5.799368e+08
            ...
9359    1.329831e+10
Length: 8700, dtype: float64
```
The estimate method also provides some diagnostic information that helps judge the quality of the regression. This information includes a listing of columns that dropped due to collinearities or an absence of trade and an indicator for over-fitting. 
```python
# Return diagnostic information (a Pandas.Series or DataFrame)
>>> fixed_effects_model_2.ppml_diagnostics
Overfit Warning                                                                 No
Collinearities                                                                 Yes
Number of Columns Excluded                                                      41
Perfectly Collinear Variables    [exporter_year_fe_ZAF2013, exporter_year_fe_ZA...
Zero Trade Variables             [importer_year_fe_ARG2015, importer_year_fe_AU...
Completion Time                                                       0.25 minutes
dtype: object

# Retrieve the full list of collinear columns
>>> fixed_effects_model_2.ppml_diagnostics['Perfectly Collinear Variables']
['exporter_year_fe_ZAF2013', 'exporter_year_fe_ZAF2014', 'exporter_year_fe_ZAF2015']
```

The gme package also features several tools to help compile and format the results for use within python or outside of it.  These tools include one method named *combine_sector_results()* for pulling all coefficients, standard errors, and p-values from from multiple sectors into a single DataFrame. The second, called *format_regression_tables*, creates formatted tables for presentation that can be exported as a text file, csv file, or LaTeX file with some stylized syntax.

```python
# Collect coefficients, standard errors, and p-values from the regression results.
>>> combined_results = fixed_effects_model_2.combine_sector_results
>>> combined_results.head()
                          all_coeff     all_pvalue              all_stderr
log_distance              -0.739840  9.318804e-211  (0.023879411125052336)
agree_pta                  0.334219   5.134355e-15   (0.04271952339258154)
common_language            0.128770   1.076932e-03   (0.03938367074719932)
contiguity                 0.255161   5.857612e-08   (0.04705076644539403)
importer_year_fe_ARG2013  26.980367   0.000000e+00    (0.3612289201097519)

# Had there been multiple sectors/regressions in the model results, there would 
# have been additional columns in the 'combined' DataFrame.

# Format the table and export to a csv file
>>> fixed_effects_model.format_regression_table(format='csv',
                                                se_below = True,
                                                omit_fe_prefix = ['importer_year',
                                                                  'exporter_year'],
                                                path = 'C:\\formatted_table.csv')

# which writes a table to the hard drive that looks like:
       Variable                 all
      agree_pta            0.334***
                            (0.043)
common_language            0.129***
                            (0.039)
     contiguity            0.255***
                            (0.047)
   log_distance           -0.740***
                            (0.024)
            AIC   9656495631872.947
            BIC   9656495371812.434
     Likelihood  -4828247815607.474
           Obs.                8700
```
It is also worth noting that the commands *combine_sector_results()* and *format_regression_tables()* can both be used in one of two ways.  They are both stand-alone functions that can be supplied dictionaries of results (produced directly from the EstimationModel or custom assembled by a user), as in the *format_regression_table()* example.  Alternatively, both can be used as methods on the EstimationObject itself, as in the *combine_sector_results()* example.
!!! tip
    **LaTeX users**: The method *format_regression_table* can output a table into a csv file with some desired LaTeX syntax. This can be done by specifying *format = '.csv'* and *'latex_syntax'=True*. This option allows users manipulate the tables in spreadsheet software while retaining LaTeX syntax.  We recommend reading the file into the spreadsheet software as 'text data' so that it does not try to interpret the formatting of the table entries. 







[^DataFrame]: See [https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html](https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html) for more information on Pandas DataFrames.

[^sector_var_name]: Had their been multiple sectors, we could have indicated so by adding the input *sector_var_name = 'sector_column'* in the declaration of the EstimationData.

[^results_dict]: Additionally, the results of the estimation are saved as a attribute of the estimation model---*EstimationModel.results_dict*---and can be retrieved that way as well.

[^statsmodels]: For more details about the *statsmodels* results object, see [http://www.statsmodels.org/0.6.1/generated/statsmodels.genmod.generalized_linear_model.GLMResults.html](http://www.statsmodels.org/0.6.1/generated/statsmodels.genmod.generalized_linear_model.GLMResults.html).