# Introduction to Python
This tutorial demonstrates some basic python concepts and syntax that are integral for working with the GME package.  Additionally, it demonstrates aspects of the *pandas* package, which provides a collection of data tools that are both a major part of the GME tools and exceptionally useful for data analysis in Python.  This tutorial is far from comprehensive, even when it comes to basic usage, but should help you become sufficiently well versed to begin working with the GME package. 



## Basic Python Concepts and Syntax


### Computation
One of the most fundamental processes is basic arithmetic.

```python
>>> 2+2
4
>>> 3*5
15
>>> (3*10)/16 + 14
15.875
```

### Variables and  Types

Variables can be used to store information for further interaction.
```python


>>> a = 16
# The variable you want to assign is on the left side, the value you want to set it to is on the right.
>>> b = 10
>>> c = a*b
>>> print(a,b,c)
16 10 160

>>> b=25
>>> c=a*b
>>> print(a,b,c)
16 25 400
```

Variables and data more broadly are much more expansive than just integers. The following is a non-exhaustive list of the data types you will frequently use.


**Integers**: (*int*) A simple number without decimal points.

```python
# The type() function returns the data type of the argument.
>>> type(12) 
<class 'int'>

>>> type(a)
<class 'int'>
```

**Float**: (*float*) A number with decimal places.
```python
>>> type(3.25)
<class 'float'>

>>> type(2**(.5))
<class 'float'>

# you can also specify the type you would like a value to take
>>> type(float(a)) 
<class 'float'>
>>> print(a)
16.0
```





 **String**: (*str*) Non-numeric characters. Strings are denoted by wrapping characters in either single or double
 quotes (e.g. ' '  or " ").
```python

>>> str_example = 'Hello World!'
>>> print(str_example)
Hello World

>>> type(str_example)
<class 'str'>

>>> type("12")
<class 'str'>

>>> type('a')
<class 'str'>

# We can also combine (concatenate) strings
>>> print("12" + "14")
1214
```




**Boolean**: (*bool*) A binary type that equals True or False

```python
>>> boolean_example = True
>>> type(boolean_example)
<class 'bool'>
```





**List**: (*list*) A list contains a series of values and, potentially, types. They are created using square brackets (e.g. [ ] )

```python
>>> list_example = [1,12,25,37,22]
>>> type(list_example)
<class 'list'>

# They are indexed
>>> list_example[0] # Square brackets denote indexes in a list. i.e. the zeroth element of list_example in this case
1
>>> list_example[3]
37
>>> list_example[1:3] # and sliceable
[12, 25]

# They can also contain other data types
>>> list_example_2 = ["This", "list","contains", 'strings', float(22.134), a, b, c]
>>> print(list_example_2)
['This', 'list', 'contains', 'strings', 22.134, 16, 25, 400]

>>> type(list_example_2[0])
<class 'str'>

>>> type(list_example_2[7])
<class 'int'>

# They can be combined
>>> list_example_3 = list_example + list_example_2
>>> list_example_3
[1, 12, 25, 37, 22, 'This', 'list', 'contains', 'strings', 22.134, 16, 25, 400]

# They can be added to
>>> list_example.append('last')
>>> print(list_example)
[1, 12, 25, 37, 22, 'last']

# and can be counted/measured
>>> len(list_example_3)
13
```


**Tuple**: (*tuple*) A tuple is similar to a list except that it's size and order is fixed. Many of the other features
 hold from lists but the inability to change the shape or order may offer some desirable protections in your code.
 They are declared using parentheses (e.g. ( ) ).

```python
>>> tuple_example = ('Hello', 25, a, c)
>>> type(tuple_example)
<class 'tuple'>

>>> tuple_example[2]
16
>>> tuple_example.append('new element')
'''
Traceback (most recent call last):
  File "<input>", line 1, in <module>
AttributeError: 'tuple' object has no attribute 'append'
'''
```



**Dictionary**: (*dict*) A dictionary is a very useful datatype which, like a list or tuple, can contain a series of values. However, it has the added feature that elements are 'keyed', such that each value is associated with a key. # The dictionary is declared using curly braces (e.g.  { } ). Within the dictionary, a key (str) is followed by a colon then the value to assign to that key (e.g. key:value = 'first':'peter') 

```python
>>> dictionary_example = {'first':'Karl','last':'Marx','job':'economist', 'ext':3186}
>>> print(dictionary_example)
{'first': 'Karl', 'last': 'Marx', 'job': 'economist', 'ext': 3186, 'location': {'city': 'Washington', 'state': 'DC'}}

>>> type(dictionary_example)
<class 'dict'>

# Dictionaries are indexed using the keys.
>>> dictionary_example['last']
'Marx'

# Can be added to by creating a new key.
>>> dictionary_example['location'] = {'city':'Washington','state':'DC'}
>>> print(dictionary_example)
{'first': 'Karl', 'last': 'Marx', 'job': 'economist', 'ext': 3186, 'location': {'city': 'Washington', 'state': 'DC'}}

>>> dictionary_example['location']['city'] # chained indexing
'Washington'

# The keys in a dictionary can be retrieved in the following way:
>>> dictionary_example.keys()
dict_keys(['first', 'last', 'job', 'ext', 'location'])
```





### Logical Operators and Decision Tests
Logical tests are a way of comparing things and performing conditional operations

```python
# Lets create some initial (int) values to work with
>>> x=10
>>> y=10
>>> z=5

>>> x == y # '=='  tests the equivalence of the left and right side
True

>>> x != y # '!='  tests the non-equivalence of both sides
False

>>> x == (y and z) # 'and' tests the equivalence to both y *AND* z
False

>>> x == (y or z) # 'or' tests the equivalence to  y *OR* z
True

>>> x > z # inequalities work as expected with '>', '<', '>=', and '<='
True

>>> x <= y
True

# Logical operators are especially useful with if statements
>>> x = 20
>>> if x > 11:
...     print('x is bigger than 11')
x is not bigger than 11

# or with 'else' statements
>>> x = 10
>>> if x > 11:
...     print('x is bigger than 11')
... else:
...     print('x is not bigger than 11')
x is not bigger than 11
```
In Python, statements are grouped by offsetting commands using tabs. Unlike many other languages that wrap statements like *if* with particular syntax like parentheses, braces, or specific begin and end statements, Python interprets things entirely based on tab indentation.  For example, a collection of commands belonging to a statement within another statement should be preceded by *two* tabs. 


### Iteration
One thing you will find very useful is the ability to automate and perform routine, repeating tasks. For loops are a useful tool for these tasks because they perform an action for each value in an 'iterable' object (e.g. a *list* or *tuple*)

```python
>>> iteration_sequence = [0,1,2,3,4]
>>> for i in iteration_sequence: # i gives the iteration value, iteration_sequence gives a (list) of values to iterate over,
...     print(i)                 # : begins the loop.  a tab indent indicates commands to be interpreted in the loop.
                                 # Unlike many languages, there is no closing statement for the loop, the indentation
                                 # fully declares the scope of the command.
0
1
2
3
4


# Suppose we wanted to use this to make some calculation (e.g. a Fibonacci Sequence)
>>> fibonacci_sequence = [1,2]
>>> for i in range(2,20):
...     next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2] # This adds the previous two entries in the (list)
...     fibonacci_sequence.append(next_number) # this adds the new number to the end of the list

>>> print(fibonacci_sequence)
[1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]

# You can also iterate on elements rather than sequential numbers
>>> dictionary_serge = {'first':'Adam','last':'Smith','job':'economist','location':{'city':'Arlington','state':'VA'}}
>>> dictionary_list = [dictionary_example, dictionary_serge] # This creates a (list) of two (dictionaries)

>>> for person in dictionary_list: # This time person is a dictionary rather than a simple index, and can be used that way
...     print('The ' + person['job'] + ' ' + person['first'] + ' ' + person['last']
...           + ' lives in ' + person['location']['city'])
...     if person['location']['state'] != 'DC':
...         person['statehood'] = True
...     else:
...         person['statehood'] = False
The economist Karl Marx lives in Washington
The economist Adam Smith lives in Arlington

>>> print(dictionary_list[0]['statehood'],dictionary_list[1]['statehood'])
False True
```


### Functions
Functions provide a way of packaging and generalizing a routine task. A function is defined using the *def* command

```python
# Lets work on generalizing the fibonacci calculation
>>> def fibonacci_nums(sequence_length): # 'def' tells python that you are about to define a function
...                                      # 'fibonacci_nums' is the name of the fucntion
...                                      # 'sequence_length' is an input to be supplied to the function
...     fibonacci_sequence = [1,2]
...     for i in range(2, sequence_length):
...         next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]  # This adds the previous two entries in the (list)
...         fibonacci_sequence.append(next_number)  # this adds the new number to the end of the list
...     return fibonacci_sequence # this determines what the function returns. In this case it is a list of fibonacci numbers

>>> fibonacci_nums(30) # Lets test the new function
[1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269]
```



## Data Manipulation and Regression Analysis
The following with provide a basic crash course in using python to perform standard econometric/data analysis tasks.  Our reccomendation for this type of work is to use the *pandas* package, which contains data manipulation tools, and the *statsmodels* package, which contains statistical tools.  For users familiar with R, you should find the syntax and programming conventions of these packages very similar to those in R.




### Importing tools
By default, python does not have a ton of tools.  Fortunately, others have written tons of them. For econometrics, we will be extensively using two: pandas, which is a data manipulation toolbox, and statsmodels, which is a statistical package (numpy, which a package for arrays, is useful too).

```python
>>> import pandas as pd
# The 'pd' gives a prefix that will be used to identify functions as coming from that package/module
>>> import statsmodels.api as sm
>>> import numpy as np
```


### Load Data
Python (or, more accurately, pandas) has a robust set of tools for loading data in in a wide range of formats such as .csv, .dta (stata), or .xls (excel). For the sake of this tutorial, we will be loading some data from the internet via a URL. Most of the time, you will probably be loading data from a file location of your computer, which uses the same synatx with a file path replacing the URL.

```python
>>> loaded_trade_data = pd.read_csv(
...     'https://www.usitc.gov/data/gravity/example_trade_and_grav_data_small.csv')
# pd.read_csv() has created a Pandas DataFrame, which is the object that contains the data.
# There are also read_excel, read_sql, read_stata, etc. versions of this function for a wide range of data file types.

# To view the data, there are several options:
>>> loaded_trade_data.head(5)  # This prints the first 5 lines of the Dataframe
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


### Working With the Data

```python

>>> loaded_data.columns   # This prints the column headers
Index(['importer', 'exporter', 'year', 'trade_value', 'agree_pta',
       'common_language', 'contiguity', 'log_distance'],
      dtype='object')
      
>>> loaded_data.shape     # Returns the dimensions of the data
(98612, 8)

>>> loaded_data.info()    # Returns some useful info such as dtypes, memory usage, dimensions.
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

>>> loaded_data.describe() # Some basic summary stats of the variables
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

>>> loaded_data['importer']  # The brackets ( [] ) are used to index or "slice" the data. In this case,
... #  it returns the entire "reporter_iso3" column.
0        AUS
1        AUS
2        AUS
        ... 
98609    VEN
98610    VEN
98611    VEN
Name: importer, Length: 98612, dtype: object

>>> loaded_data.loc[3, "importer"]  # The command ".loc" can be used to identify specific row and column indexes
'AUS'

# Suppose we wanted to figure out what countries are present as exporting partners in the data:
>>> partner_countries = loaded_data['exporter'].unique()
>>> num_of_partners = len(partner_countries)
>>> print(num_of_partners)
62

# Suppose we wanted to summarize the data by country
>>> trade_data_temp = loaded_data.groupby('importer')  # Creates a modified dataframe where observations
# are grouped by reporter (and saved to a new object to avoid over-writting the original
>>> imports_summary = trade_data_temp['trade_value'].agg(['mean', 'max', 'count'])  # this returns a DataFrame with the
# desired stats for each 'group'.
>>> imports_summary = imports_summary.reset_index()  # By default, the groups get turned into index labels. the reset_index()
# command turns them back into a column, which is generally useful.


# Suppose we wanted to drop the distance variable.
>>> trade_data = loaded_data.drop('log_distance', axis=1)  # This drops the column (axis = 1) 'log_distance',
# or alternatively, suppose we wanted to keep only the trade data and identifiers.
>>> trade_data = loaded_data[['importer', 'exporter', 'year', 'trade_value']]  # would do the same
# thing by returning only the specified list of columns.
#Perhaps we want to rename a column
>>> trade_data = trade_data.rename(columns={'trade_value': 'bilateral_trade'})

# How can we deal with missing values?
>>> trade_data = trade_data.dropna(how='any')  # This drops 'n/a' rows if they appear in 'any' column.
>>> loaded_data.shape, trade_data.shape  # Check to see if we lost any rows.
((98612, 8), (84924, 4))

# How can we subset the data based on a condition?
>>> trade_data = trade_data[trade_data['year'] > 1992]


# suppose we wanted to save this modified trade dataset.
trade_data.to_csv("C:Documents\\modified_trade_data.csv")

```



```python
# Lets now create a dataset of only the gravity variables
>>> gravity_data = loaded_data[['importer', 'exporter', 'year', 'agree_pta',
...        'common_language', 'contiguity', 'log_distance']]

# Next, lets merge the gravity data back onto to the trade data
>>> estimation_data = pd.merge(left=trade_data,  # left: the first of two datasets to merge
...                            right=gravity_data,  # right: the second dataset,
...                            how='left',  # this specifies the type of merge ('left', 'right', 'inner', 'outer')
...                            left_on=['importer', 'exporter', 'year'],
...                            # A list of columns to merge on in the left dataset
...                            right_on=['importer', 'exporter', 'year']  # A list of columns to merge on in the right dataset
...                            )  # Note that the right_on and left_on lists should be in corresponding orders.
# Merge Types:
#   'inner' - retains only rows in which their are matches in both dataframes (i.e. _merge = 3 in stata)
#   'outer' - retains all rows from both dataframes, even if they did not match (i.e. _merge = 3 & 1 & 2)
#   'left'  - retains all rows from the left dataframe, with or without matches  (i.e. _merge = 3 & 1)
#   'right' - retains all rows from the right dataframe, with or without matches (i.e. _merge = 3 & 2)

>>> estimation_data.head(5)
  importer exporter  year  bilateral_trade  agree_pta  common_language  \
0      ARG      AUS  1993     7.353949e+07        0.0              1.0   
1      ARG      BOL  1993     1.077911e+08        1.0              1.0   
2      ARG      BRA  1993     3.566469e+09        1.0              1.0   
3      ARG      CAN  1993     8.783576e+07        0.0              1.0   
4      ARG      CHE  1993     1.639864e+08        0.0              1.0   
   contiguity  log_distance  
0         0.0      9.398793  
1         1.0      7.536893  
2         1.0      7.783794  
3         0.0      9.152224  
4         0.0      9.327306  

>>> estimation_data = estimation_data.dropna(how='any')  # drop any rows missing gravity data


```python
# Our dataset contains some zero trade flows, lets drop them
>>> positive_trade_rows = estimation_data['bilateral_trade'] != 0 # Identify rows with positive trade
>>> estimation_data = estimation_data.loc[positive_trade_rows,:] # This returns the rows identified in the previous steps
                                                             # and all columns (:).

# Create a new variable with log trade
>>> estimation_data['log_trade'] = np.log(estimation_data['bilateral_trade'])


# Create Dummy variables
>>> importer_fixed_effects = pd.get_dummies(data=estimation_data['importer'], prefix='imp_fe')  # data specifies what
# column should be used as the ID for dummies, 'prefix' is an option that lets you name the fixed effects
>>> importer_fixed_effects.head(1)
   imp_fe_ARG  imp_fe_AUS  imp_fe_AUT  imp_fe_BEL  imp_fe_BOL  imp_fe_BRA  \
0           1           0           0           0           0           0   
   imp_fe_CAN  imp_fe_CHE  imp_fe_CHL  imp_fe_CHN     ...      imp_fe_SDN  \
0           0           0           0           0     ...               0   
   imp_fe_SGP  imp_fe_SWE  imp_fe_THA  imp_fe_TUN  imp_fe_TUR  imp_fe_URY  \
0           0           0           0           0           0           0   
   imp_fe_USA  imp_fe_VEN  imp_fe_ZAF  
0           0           0           0  
[1 rows x 61 columns]

>>> exporter_fixed_effects = pd.get_dummies(estimation_data['exporter'], prefix='exp_fe')  # repeat for exporters
>>> exporter_fixed_effects = exporter_fixed_effects.drop('exp_fe_ZAF', axis=1)  # drop a column to avoid collinearity

# Split the data into right side and left side variables
>>> lhs_data = estimation_data[['log_trade']]
>>> rhs_data = estimation_data[['log_distance', 'contiguity', 'agree_pta', 'common_language']]

# Add the dummies to the right hand variables
>>> rhs_data = pd.concat(objs=[rhs_data, importer_fixed_effects, exporter_fixed_effects], axis=1)  # concatinate
# is a method of combining two datasets that does not rely on merging/joining on keys, it does so on rows or columns
# 'objs' is a list of DataFrames to concatinate (they need to have the same row or column IDs as each other)
# 'axis' specifies whether you want to concatinate rows or colomns. axis = 1 specifies that the columns are to be
# combined (i.e. horizontal combining)

>>> rhs_data.columns
Index(['log_distance', 'contiguity', 'agree_pta', 'common_language',
       'imp_fe_ARG', 'imp_fe_AUS', 'imp_fe_AUT', 'imp_fe_BEL', 'imp_fe_BOL',
       'imp_fe_BRA',
       ...
       'exp_fe_SDN', 'exp_fe_SGP', 'exp_fe_SWE', 'exp_fe_THA', 'exp_fe_TUN',
       'exp_fe_TUR', 'exp_fe_TWN', 'exp_fe_URY', 'exp_fe_USA', 'exp_fe_VEN'],
      dtype='object', length=126)
```


### Estimation

```python
>>> ols_model = sm.OLS(lhs_data, rhs_data)  # This step is a little odd. It creates a python "regression object", to which
# various other OLS fuctions can be applied

>>> ols_results = ols_model.fit()  # .fit() is probably the most important function as it returns an object with
# the estimated results.

>>> ols_results.summary()  # returns the results in a standard format
<class 'statsmodels.iolib.summary.Summary'>
"""
                            OLS Regression Results                            
==============================================================================
Dep. Variable:              log_trade   R-squared:                       0.760
Model:                            OLS   Adj. R-squared:                  0.760
Method:                 Least Squares   F-statistic:                     1882.
Date:                Wed, 01 Aug 2018   Prob (F-statistic):               0.00
Time:                        12:31:34   Log-Likelihood:            -1.3837e+05
No. Observations:               74384   AIC:                         2.770e+05
Df Residuals:                   74258   BIC:                         2.781e+05
Df Model:                         125                                         
Covariance Type:            nonrobust                                         
===================================================================================
                      coef    std err          t      P>|t|      [0.025      0.975]
-----------------------------------------------------------------------------------
log_distance       -1.1302      0.012    -96.040      0.000      -1.153      -1.107
contiguity          0.2422      0.037      6.582      0.000       0.170       0.314
agree_pta           0.1996      0.016     12.687      0.000       0.169       0.230
common_language     0.6633      0.018     37.904      0.000       0.629       0.698
imp_fe_ARG         28.3824      0.135    210.554      0.000      28.118      28.647
...                    ...        ...        ...        ...         ...         ...
(truncated for the tutorial)
exp_fe_USA          3.2536      0.062     52.103      0.000       3.131       3.376
exp_fe_VEN         -2.2117      0.063    -35.183      0.000      -2.335      -2.088
==============================================================================
Omnibus:                    13854.709   Durbin-Watson:                   1.701
Prob(Omnibus):                  0.000   Jarque-Bera (JB):            70317.321
Skew:                          -0.814   Prob(JB):                         0.00
Kurtosis:                       7.476   Cond. No.                     1.46e+03
==============================================================================
Warnings:
[1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
[2] The condition number is large, 1.46e+03. This might indicate that there are
strong multicollinearity or other numerical problems.
"""

>>> ols_results.params  # returns only the parameter values
log_distance       -1.130207
contiguity          0.242191
agree_pta           0.199577
common_language     0.663323
imp_fe_ARG         28.382397
imp_fe_AUS         29.955248
                     ...    
exp_fe_USA          3.253590
exp_fe_VEN         -2.211676
Length: 126, dtype: float64

>>> ols_results.rsquared  # The r squared values
0.7600680070806417

>>> ols_results.HC1_se  # Huber/White standard errors. You could also return this originally with ols_model.fit(cov_type = 'HC1')
log_distance       0.011628
contiguity         0.036585
agree_pta          0.016563
common_language    0.017452
imp_fe_ARG         0.129097
imp_fe_AUS         0.125993
                     ...   
exp_fe_USA         0.038809
exp_fe_VEN         0.069779
Length: 126, dtype: float64

ols_results.pvalues  # pvalueslog_distance        0.000000e+00
contiguity          4.682417e-11
agree_pta           7.591490e-37
common_language     0.000000e+00
imp_fe_ARG          0.000000e+00
imp_fe_AUS          0.000000e+00
                       ...      
exp_fe_USA          0.000000e+00
exp_fe_VEN         6.068582e-269
Length: 126, dtype: float64

```



### Saving the results
There are many different way to export results including writing tables to a text file, saving estimates in a csv dataset, storing the python objects themselves.  In this tutorial, we will look at the first two options. For the third option, see the *pickle* package.

To write the results to a text file, you need to 'open' a text file on the hard drive, write the results to the file, and close the file.
```python
>>> text_file = open("C:\\Documents\\regression_results.txt", "w")
>>> text_file.write(ols_results.summary().as_text())
>>> text_file.close()
```

Alternatively, you could export some of these results to excel.
```python
>>> type(ols_results.params)  # Statsmodels conveniently returns Pandas Objects, so we can feed them into a dataframe
<class 'pandas.core.series.Series'>

>>> results_dataframe = pd.concat(
...     {'coefficients': ols_results.params, 'SE': ols_results.HC1_se, 'p_values': ols_results.pvalues}, axis=1)
>>> results_dataframe.head(5)
                       SE  coefficients      p_values
log_distance     0.011628     -1.130207  0.000000e+00
contiguity       0.036585      0.242191  4.682417e-11
agree_pta        0.016563      0.199577  7.591490e-37
common_language  0.017452      0.663323  0.000000e+00
imp_fe_ARG       0.129097     28.382397  0.000000e+00

>>> results_dataframe.to_csv("C:\\Documents\\regression_results.csv")
```

