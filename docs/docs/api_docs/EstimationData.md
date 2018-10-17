## Class
**gme.EstimationData**(
                 *data_frame=None,
                 name:str='unnamed',
                 imp_var_name:str='importer',
                 exp_var_name:str='exporter',
                 year_var_name:str='year',
                 trade_var_name:str=None,
                 sector_var_name:str=None,
                 notes:List[str]=[]*)
                 
## Description
An object used for storing data for gravity modeling and producing some summary statistics.


## Arguments
**data_frame**: *Pandas.DataFrame*<br> 
 &emsp; A DataFrame containing trade, gravity, etc. data. 
 
**name**: (optional) *str*<br> 
 &emsp; A name for the dataset.
  
**imp_var_name**: *str*<br> 
 &emsp; The name of the column containing importer IDs.
  
**exp_var_name**: *str*<br> 
 &emsp; The name of the column containing exporter IDs.
  
**year_var_name**: *str*<br> 
 &emsp; The name of the column containing year data. 
 
**trade_var_name**: (optional) *str*<br> 
 &emsp; The name of the column containing trade data. 
 
**sector_var_name**: (optional) *str*<br> 
 &emsp; The name of the column containing sector/industry/product IDs.
  
**notes**: (optional) *str*<br> 
 &emsp; A string to be included as a note n the object. 
 
## Attributes
**data_frame**: *Pandas.DataFrame*<br> 
 &emsp; The supplied DataFrame. 

**name**: *str*<br> 
 &emsp; The supplied data name. 

**imp_var_name**: *str*<br> 
 &emsp; The name of the column containing importer IDs. 

**exp_var_name**: *str*<br> 
 &emsp; The name of the column containing exporter IDs. 

**year_var_name**: *str*<br> 
 &emsp; The name of the column containing year data. 

**trade_var_name**: *str*<br> 
 &emsp; The name of the column containing trade data. 

**sector_var_name**: *str*<br> 
 &emsp; The name of the column containing sector/industry/product IDs. 

**notes**: *List[str]*<br> 
 &emsp; A list of notes. 

**number_of_exporters**: *int*<br> 
 &emsp; The number of unique exporter IDs in the dataset. 

**number_of_importers**: *int*<br> 
 &emsp; The number of unique importer IDs in the dataset. 

**shape**: *List[int]*<br> 
 &emsp; The dimensions of the dataset. 

**countries**: *List[str]*<br> 
 &emsp; A list of the unique country IDs in the dataset. 

**number_of_countries**: *int*<br> 
 &emsp; The number of unique country IDs in the dataset. 

**number_of_years**: *int*<br> 
 &emsp; The number of years in the dataset 

**columns**: *List[str]*<br> 
 &emsp; A list of column names in the dataset. 

**number_of_sectors**: *int*<br> 
 &emsp; If a sector is specified, the number of unique sector IDs in the dataset. 



## Methods
**tablulate_by_group**:<br> 
 &emsp; Summarize columns by a user-specified grouping. Can be used to tabulate, aggregate, <br> 
 &emsp; summarize,etc. data.

 &emsp; **Arguments:** <br> 
 
 &emsp;&emsp; **tab_variables**: *List[str]* <br> 
        &emsp;&emsp;&emsp; Column names of variables to be tabulated
        
 &emsp;&emsp; **by_group**: *List[str]* <br>
        &emsp;&emsp;&emsp; Column names of variables by which to group observations for tabulation.
 
 &emsp;&emsp; **how**: *List[str]* <br>
         &emsp;&emsp;&emsp; The method by which to combine observations within a group. Can accept <br>
         &emsp;&emsp;&emsp; 'count', 'mean',  'median', 'min', 'max', 'sum', 'prod', 'std', and 'var'. It may work <br>
         &emsp;&emsp;&emsp; with other numpy or pandas functions.

&emsp;**Returns**: *Pandas.DataFrame* <br> 
    &emsp;&emsp; A DataFrame of tabulated values for each group.

          
            
         
**year_list**:<br> 
 &emsp; Returns a list of years present in the data. 


**countries_each_year**:<br> 
 &emsp; Returns a dictionary keyed by year ID containing a list of country IDs present in each <br> 
 &emsp; corresponding year. <br>



**sector_list**:<br> 
 &emsp;   Returns a list of unique sector IDs 

**dtypes**:<br> 
 &emsp; Returns the data types of the columns in the EstimationData.data_frame using<br> 
 &emsp; Pandas.DataFrame.dtypes(). See Pandas documentation for more information.
    

**info**:<br> 
 &emsp; Print summary information about EstimationData.data_frame using<br> 
 &emsp; Pandas.DataFrame.dtypes(). See Pandas documentation for more information.

**describe**:<br> 
 &emsp; Generates some descriptive statistics for EstimationData.data_frame using<br> 
 &emsp; Pandas.DataFrame.describe(). See Pandas documentation for more information.

**add_note**:<br> 
 &emsp; Add a note to the list of notes in 'notes' attribute.
    
&emsp; **Arguments**: <br>

&emsp;&emsp; **note**: *str* <br>
&emsp;&emsp;&emsp; A note to add to EstimationData. <br>
     
&emsp; **Returns**: *None*



## Examples
```python
# Load a DataFrame
>>> import pandas as pd
>>> gravity_data = pd.read_csv('https://www.usitc.gov/data/gravity/example_trade_and_grav_data_small.csv')
>>> gravity_data.head(5)
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

example_estimation_data = EstimationData(gravity_data,
                                 imp_var_name='importer',
                                 exp_var_name='exporter',
                                 trade_var_name='trade_value',
                                 year_var_name='year',
                                 notes='Downloaded from https://www.usitc.gov/data/gravity/example_trade_and_grav_data_small.csv')

# tabulate_by_group
# Sum trade value by importer and year
>>> aggregated_data = example_estimation_data.tabulate_by_group(tab_variables = ['trade_value'],
...                                                         by_group = ['importer', 'year'],
...                                                         how = ['sum'])
>>> aggregated_data.head(5)
  importer_  year_  trade_value_sum
0       ARG   1989     0.000000e+00
1       ARG   1990     0.000000e+00
2       ARG   1991     0.000000e+00
3       ARG   1992     0.000000e+00
4       ARG   1993     1.593530e+10

# Summarize minimum and maximum trade flows between each trading pair
>>> summarized_data = example_estimation_data.tabulate_by_group(tab_variables = ['trade_value'],
...                                                         by_group = ['importer', 'exporter'],
...                                                         how = ['min','max'])
>>> summarized_data.head(5)
  importer_ exporter_  trade_value_min  trade_value_max
0       ARG       AUS              0.0     4.095529e+08
1       ARG       AUT              0.0     2.986187e+08
2       ARG       BEL              0.0     7.669537e+08
3       ARG       BOL              0.0     2.743706e+09
4       ARG       BRA              0.0     2.218091e+10

# year_list
>>> example_estimation_data.year_list()
[1989,
 1990,
 1991,
 1992,
 ...

# countries_each_year
>>> countries = example_estimation_data.countries_each_year()
>>> countries.keys()
dict_keys([1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015])
>>> countries[1989]
['ESP',
 'SGP',
 'PHL',
 'NGA',
 'VEN',
 ...

# dtypes
>>> example_estimation_data.dtypes()
importer            object
exporter            object
year                 int64
trade_value        float64
agree_pta          float64
common_language    float64
contiguity         float64
log_distance       float64
dtype: object

>>> example_estimation_data.info()
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

# describe
>>> example_estimation_data.describe()
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

# notes
>>> example_estimation_data.add_note('year IDs are integers')
>>> example_estimation_data.notes
['Downloaded from https://www.usitc.gov/data/gravity/example_trade_and_grav_data_small.csv',
'year IDs are integers']
```

