# Getting Started

## Preparing the Software

### Dependencies

The GME package requires pandas, statsmodels, patsy, and scipy packages. If not already present on your system, they will be automatically installed when installing GME.

### Installation

Download and install the GME package.

[//]: # (???+ tip)
[//]: #   (Easily copy the code below by using the copy button in the upper right corner of the code block.)  
    
```python
pip install gme
```

## A Basic Example: Run PPML estimation

### Step 1. Import the needed packages
``` python
import gme as gme
import pandas as pd
```

### Step 2. Create EstimationData

The GME package is built upon a specialized data object called EstimationData. EstimationData contains data in a [Pandas DataDrame](http://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe) as well as a collection of additional information and tools that are useful for gravity modeling, such as 

* A log of the history of the data, such as the location of the file it was read from and modifications made to it,
* Metadata, such as names of the columns containing importer, exporter, and year information, so that they need not be continuously supplied,
* Several tools for producing summary statistics or other types of commonly sought descriptive information.

Begin by loading example trade data.  The dataset used in the following code is [available for download](https://www.usitc.gov/data/gravity/example_trade_and_grav_data_small.csv) or can be accessed directly with python and pandas, as shown below.

```python
sample_data = pd.read_csv(
    'https://www.usitc.gov/data/gravity/example_trade_and_grav_data_small.csv')
print(sample_data.head())
```
The first command above reads the data file into memory while the second shows the column names and first 5 lines of the data file.
```console
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
```

Next, create an instance of the EstimationData object using the sample data. To create an EstimationData instance (called gme_data in the example below), you need to supply a Pandas DataFrame and identifiers for certain key columns, such as the trade flows, importer/exporter, year, and sector (if applicable).


```python
gme_data = gme.EstimationData(data_frame = sample_data,
                              imp_var_name = 'importer',
                              exp_var_name = 'exporter',
                              trade_var_name = 'trade_value',
                              year_var_name = 'year')
print(gme_data)
```
The print command above produces basic summary statistics, contained in a printable representation of the EstimationData class:
[//]: # (CP: The definition above refers to the __repr__ method which is used in the Estimation data command. See here: https://stackoverflow.com/questions/1984162/purpose-of-pythons-repr )

```console
number of countries: 62 
number of exporters: 62 
number of importers: 62 
number of years: 27 
number of sectors: not_applicable 
dimensions: (98612, 8)
```

### Step 3. Create an EstimationModel
After creating an EstimationData object, you need to create an EstimationModel object, which will be used to produce gravity estimates.  To create an EstimationModel instance (called gme_model in the example below), you need to supply an EstimationData object and a specification.

```python
gme_model = gme.EstimationModel(estimation_data = gme_data,
                                lhs_var = 'trade_value',
                                rhs_var = ['log_distance','agree_pta','common_language','contiguity'],
                                fixed_effects = ['importer', 'exporter'],
                                keep_years = [2015])
```

The initialization of EstimationModel establishes a reference to the EstimationData object rather than a copy of the data.

[//]: # (SS: People may be worried here that we are creating three copies of the data in memory: gme_data, EstimationData, and EstimationModel. Does Python copy the data in this case or just saves a pointer to gme_data?)

### Step 4. Estimate the model

??? Info "What is a method?"
    A method is a function that is connected only to a particular object. [Click here to see the relevant Python documentation.](https://docs.python.org/3/tutorial/classes.html#instance-objects)
    
Once the EstimationModel is defined, it can be estimated by applying the method .estimate()

[//]: # (gme_results = gme_model.estimate())
```python
gme_model.estimate()
```

The code provides some information while it is running:

```console
select specification variables: ['log_distance', 'agree_pta', 'common_language', 'contiguity', 'trade_value', 'importer', 'exporter', 'year'], Observations excluded by user: {'rows': 0, 'columns': 0}
drop_intratrade: no, Observations excluded by user: {'rows': 0, 'columns': 0}
drop_imp: none, Observations excluded by user: {'rows': 0, 'columns': 0}
drop_exp: none, Observations excluded by user: {'rows': 0, 'columns': 0}
keep_imp: all available, Observations excluded by user: {'rows': 0, 'columns': 0}
keep_exp: all available, Observations excluded by user: {'rows': 0, 'columns': 0}
drop_years: none, Observations excluded by user: {'rows': 0, 'columns': 0}
keep_years: [2015], Observations excluded by user: {'rows': 94952, 'columns': 0}
drop_missing: yes, Observations excluded by user: {'rows': 0, 'columns': 0}
Estimation began at 08:09 AM  on Oct 16, 2018
Omitted Columns: ['importer_fe_ARG', 'importer_fe_AUT', 'importer_fe_BEL', 'importer_fe_CHN', 'importer_fe_COL', 'importer_fe_DZA', 'importer_fe_EGY', 'importer_fe_GHA', 'importer_fe_IDN', 'importer_fe_IRN', 'importer_fe_ISR', 'importer_fe_KEN', 'importer_fe_KOR', 'importer_fe_KWT', 'importer_fe_LBY', 'importer_fe_MAR', 'importer_fe_NGA', 'importer_fe_NLD', 'importer_fe_PAK', 'importer_fe_SAU', 'importer_fe_SGP', 'importer_fe_THA', 'importer_fe_TUN', 'importer_fe_TWN', 'importer_fe_URY', 'importer_fe_VEN', 'importer_fe_ZAF']
Estimation completed at 08:09 AM  on Oct 16, 2018
```

The results are stored in a collection (called dictionary in Python) with each sector having its own set of results. If no sectors were supplied or used, there would be only one set of results in the dictionary, labeled 'all'.


A simple table with regression results can be produced with the following command: 

```python
gme_model.format_regression_table(format = "txt")
```
which produces the regression results:
```console                                
                             Variable                all
a_agree_pta                 agree_pta           0.338***
a_agree_pta_se                                   (0.088)
a_common_language     common_language              0.063
a_common_language_se                             (0.071)
a_contiguity               contiguity           0.211***
a_contiguity_se                                  (0.085)
a_exporter_fe_ARG     exporter_fe_ARG             -0.444
a_exporter_fe_ARG_se                             (0.365)
a_exporter_fe_AUS     exporter_fe_AUS              0.619
a_exporter_fe_AUS_se                             (0.500)
                               ...                ...
a_importer_fe_USA     importer_fe_USA          30.791***
a_importer_fe_USA_se                             (0.562)
a_log_distance           log_distance          -0.784***
a_log_distance_se                                (0.051)
b_aic                             AIC  1806014725995.581
b_bic                             BIC  1806014667986.696
b_llf                      Likelihood   -903007362899.79
b_nobs                           Obs.               2040                                
```
