
########################################################################################################################
# 1. BASIC INTERACTION
########################################################################################################################


##################
# [Computation]
# Python can be used for basic arithmetic calculations
##################
2+2
3*5
(3*10)/16 + 14




##################
# [Variables]
# Variables can be used to store information for further interaction.
##################
a = 16
# The variable you want to assign is on the left side, the value you want to set it to is on the right.
b = 10
c = a*b
print(a,b,c)

b=25
c=a*b
print(a,b,c)






########################################################################################################################
# 2. TYPES
#Variables and data more broadly are much more expansive than just integers. The following is a non-exhaustive list of
#the data types you will frequently use.
########################################################################################################################


###########
# Integers: (int) A simple number without decimal points'''
###########
type(12) # The type() function returns the data type of the argument.
type(a)


'''Float: (float) A number with the availability of decimals'''
type(3.25)
type(2**(.5))
type(float(a)) # you can also specify the type you would like a value to take





##########
# String: (str) Non-numeric characters. Strings are denoted by wrapping characters in either single or double
# quotes (e.g. ' '  or " ").
##########
str_example = 'Hello World!'
print(str_example)
type(str_example)
type("12")
type('a')
# What happens when we add two strings together?
print("12" + "14")




##################
# Boolean: (bool) A binary type that equals True or False
##################
boolean_example = True
type(boolean_example)




##############
# List: (list) A list contains a series of values and, potentially, types. They are created using square brackets
# (e.g. [ ] )
##############
list_example = [1,12,25,37,22]
type(list_example)

# They are indexed
list_example[0] # Square brackets denote indexes in a list. i.e. the zeroth element of list_example in this case
list_example[3]
list_example[1:3] # and sliceable

# They can also contain other data types
list_example_2 = ["This", "list","contains", 'strings', float(22.134), a, b, c]
print(list_example_2)
type(list_example_2[0])
type(list_example_2[7])

# They can be combined
list_example_3 = list_example + list_example_2
list_example_3

# They can be added to
list_example.append('last')
print(list_example)

# and can be counted/measured
len(list_example_3)




########
# Tuple: (tuple) A tuple is similar to a list except that it's size and order is fixed. Many of the other features
# hold from lists but the inability to change the shape or order may offer some desirable protections in your code.
# They are declared using parentathese (e.g. ( ) ).
########
tuple_example = ('Hello', 25, a, c)
type(tuple_example)
tuple_example[2]
tuple_example.append('new element')




#############
# Dictionary: (dict) A dictionary is a very useful datatype which, like a list or tuple, can contain a series of
# values. However, it has the added feature that elements are 'keyed', such that each value is associated with a key.'''
#############
dictionary_example = {'first':'Karl','last':'Marx','job':'economist', 'ext':3186}
# The dictionary is declared using curly braces (e.g.  { } ). Within the dictionary, a key (str) is followed by a
# colon then the value to assign to that key (e.g. key:value = 'first':'peter')
print(dictionary_example)
type(dictionary_example)
# Dictionaries are indexed using the keys.
dictionary_example['last']
# Can be added to by creating a new key.
dictionary_example['location'] = {'city':'Washington','state':'DC'}
print(dictionary_example)
dictionary_example['location']['city'] # chained indexing

dictionary_example.keys()
# Why are lists and dictionaries important?
# In addition to being really useful on their own, the data storage method covered later is much like a list
# of dictionaries






########################################################################################################################
# 4. Logical Operators and Decision Tests
# Logical tests, including if statements are a way of comparring things and performing conditional operations
########################################################################################################################
# Lets create some initial (int) values
x=10
y=10
z=5

x == y # '=='  tests the equivalence of the left and right side
x != y # '!='  tests the non-equivalence of both sides
x == (y and z) # 'and' tests the equivalence to both y *AND* z
x == (y or z) # 'or' tests the equivalence to  y *OR* z
x > z # inequalities work as expected with '>', '<', '>=', and '<='
x <= y

# Logical operators are especially useful with if statements
if x > 11:
    print('x is bigger than 11')

x = 20

# or with 'else' statements
x = 10
if x > 11:
    print('x is bigger than 11')
else:
    print('x is not bigger than 11')







########################################################################################################################
# 4. ITERATION
# One thing you will find very useful is the ability to automate and perform routine, repeating tasks
########################################################################################################################

##################
# For loops: for loops are a way of performing an action for each value in an 'iterable' object (i.e. a list, tuple,
# or dictionary)
##################
iteration_sequence = [0,1,2,3,4,5,6,7,8,9,10]
for i in iteration_sequence: # i gives the iteration value, iteration_sequence gives a (list) of values to iterate over,
    print(i)                 # : begins the loop.  a tab indent indicates commands to be interpreted in the loop.
                             # Unlike many languages, there is no closing statement for the loop, the indentation
                             # fully declares the scope of the command.


# Suppose we wanted to use this to make some calculation (e.g. a Fibonacci Sequence)
fibonacci_sequence = [1,2]
for i in range(2,20):
    next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2] # This adds the previous two entries in the (list)
    fibonacci_sequence.append(next_number) # this adds the new number to the end of the list

print(fibonacci_sequence)

# You can also iterate on elements rather than sequential numbers
dictionary_serge = {'first':'Serge','last':'Shikher','job':'economist','location':{'city':'Arlington','state':'VA'}}
dictionary_list = [dictionary_example, dictionary_serge] # This creates a (list) of two (dictionaries)

for person in dictionary_list: # This time person is a dictionary rather than a simple index, and can be used that way
    print('The ' + person['job'] + ' ' + person['first'] + ' ' + person['last']
          + ' lives in ' + person['location']['city'])
    if person['location']['state'] != 'DC':
        person['statehood'] = True
    else:
        person['statehood'] = False

print(dictionary_list[0]['statehood'],dictionary_list[1]['statehood'])




#######
# FUNCTIONS
# Functions provide a way of packaging and generalizing a routine task
#######
#Lets work on generalizing the fibonacci calculation

def fibonacci_nums(sequence_length): # 'def' tells python that you are about to define a function
                                     # 'fibonacci_nums' is the name of the fucntion
                                     # 'sequence_length' is an input to be supplied to the function
    fibonacci_sequence = [1,2]
    for i in range(2, sequence_length):
        next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[
            i - 2]  # This adds the previous two entries in the (list)
        fibonacci_sequence.append(next_number)  # this adds the new number to the end of the list
    return fibonacci_sequence # this determines what the function returns. In this case it is a list of fibonacci numbers

fibonacci_nums(30) # Lets test the new function










#######################################
# [Performing Econometrics with Python]
# The following with provide a basic crash course in using python to perform standard econometric/data analysis tasks.
#######################################


#########################
# Step 1: Importing tools
# By default, python does not have a ton of tools.  Fortunately, others have written tons of them. For econometrics,
# we will be extensively using two: pandas, which is a data manipulation toolbox, and statsmodels, which is a
# statistical package (numpy, which a package for arrays, is useful too).
#########################

import pandas as pd
# The 'pd' gives a prefix that will be used to identify functions as coming from that package/module
import statsmodels.api as sm
import numpy as np




##########################
# Step 2: Load Data
# Python (or, more accurately, pandas) has a robust set of tools for loading data in in a wide range of formats such
# as .csv, .dta (stata), or .xls (excel)
##########################
loaded_data = pd.read_csv(
    'https://www.usitc.gov/data/gravity/example_trade_and_grav_data_small.csv')
# pd.read_csv() has created a Pandas DataFrame, which is the object that contains the data.
# Note the use of two slashes (\\). A slash on its own denotes that the following character is special (e.g. \n implies
# a carriage return). The double slash correctly denotes that there is a special character and that the character
# is a slash.
# stata_data = pd.read_stata(data_path) # This would load a .dta file
# There are also read_excel, read_sql, etc. versions for a wide range of data file types.

# To view the data, there are several options:
loaded_data.head(5)  # This prints the first 10 lines of the Dataframe
# Many IDE's also have an ability to display the data. In PyCharm, you click "Show Variables" in the Python Console
# toolbar, the click "...View as DataFrame" next to the dataframe you'd like to view.
# inputing the variable name itself will print a large number of rows or the whole thing if it is not too large large.







##########################
# Step 3: Working With the Data
# Compared to excel or stata, working with the data may feel like it has a bit of a learning curve but the speed and
# flexibility provided by python makes it well worth it to learn!
##########################


loaded_data.columns   # This prints the column headers
loaded_data.shape     # Returns the dimensions of the data
loaded_data.info()    # Returns some useful info such as dtypes, memory usage, dimensions.
loaded_data.describe() # Some basic summary stats of the variables

loaded_data['importer']  # The brackets ( [] ) are used to index or "slice" the data. In this case,
#  it returns the entire "reporter_iso3" column.

loaded_data.loc[3, "importer"]  # The command ".loc" can be used to identify specific row and column indexes

# Suppose we wanted to figure out what countries are present as exporting partners in the data:
partner_countries = loaded_data['exporter'].unique()
num_of_partners = len(partner_countries)
print(num_of_partners)
# Suppose we wanted to summarize the data by country
trade_data_temp = loaded_data.groupby('importer')  # Creates a modified dataframe where observations
# are grouped by reporter (and saved to a new object to avoid over-writting the original
imports_summary = trade_data_temp['trade_value'].agg(['mean', 'max', 'count'])  # this returns a DataFrame with the
# desired stats for each 'group'.
imports_summary = imports_summary.reset_index()  # By default, the groups get turned into index labels. the reset_index()
# command turns them back into a column, which is generally useful.


# Suppose we wanted to drop the distance variable.
trade_data = loaded_data.drop('log_distance', axis=1)  # This drops the column (axis = 1) 'log_distance',
# or alternatively, suppose we wanted to keep only the trade data and identifiers.
trade_data = loaded_data[['importer', 'exporter', 'year', 'trade_value']]  # would do the same
# thing by returning only the specified list of columns.
#Perhaps we want to rename a column
trade_data = trade_data.rename(columns={'trade_value': 'bilateral_trade'})

# How can we deal with missing values?
trade_data = trade_data.dropna(how='any')  # This drops 'n/a' rows if they appear in 'any' column.
loaded_data.shape, trade_data.shape  # Check to see if we lost any rows.

# How can we subset the data based on a condition?
trade_data = trade_data[trade_data['year'] > 1992]


# suppose we wanted to save this modified trade dataset.
# trade_data.to_csv("C:Documents\\modified_trade_data.csv")





######################
# Step 3: Merging Data
# In addition to trade data, we need to add some gravity variables.
######################

# Lets now create a dataset of only the gravity variables
gravity_data = loaded_data[['importer', 'exporter', 'year', 'agree_pta',
       'common_language', 'contiguity', 'log_distance']]

# Next, lets merge the gravity data back onto to the trade data
estimation_data = pd.merge(left=trade_data,  # left: the first of two datasets to merge
                           right=gravity_data,  # right: the second dataset,
                           how='left',  # this specifies the type of merge ('left', 'right', 'inner', 'outer')
                           left_on=['importer', 'exporter', 'year'],
                           # A list of columns to merge on in the left dataset
                           right_on=['importer', 'exporter', 'year']  # A list of columns to merge on in the right dataset
                           )  # Note, the right_on and left_on lists should be in corresponding orders.
# Merge Types:
#   'inner' - retains only rows in which their are matches in both dataframes (i.e. _merge = 3 in stata)
#   'outer' - retains all rows from both dataframes, even if they did not match (i.e. _merge = 3 & 1 & 2)
#   'left'  - retains all rows from the left dataframe, with or without matches  (i.e. _merge = 3 & 1)
#   'right' - retains all rows from the right dataframe, with or without matches (i.e. _merge = 3 & 2)

estimation_data.head(5)

estimation_data = estimation_data.dropna(how='any')  # drop any rows missing gravity data






#########################
# Step 4 Prepping the Data for Estimation
#########################
# Our dataset contains some zero trade flows, lets drop them
positive_trade_rows = estimation_data['bilateral_trade'] != 0 # Identify rows with positive trade
estimation_data = estimation_data.loc[positive_trade_rows,:] # This returns the rows identified in the previous steps
                                                             # and all columns (:).

# Create a new variable with log trade
estimation_data['log_trade'] = np.log(estimation_data['bilateral_trade'])


# Create Dummy variables
importer_fixed_effects = pd.get_dummies(data=estimation_data['importer'], prefix='imp_fe')  # data specifies what
# column should be used as the ID for dummies, 'prefix' is an option that lets you name the fixed effects
importer_fixed_effects.head(1)

exporter_fixed_effects = pd.get_dummies(estimation_data['exporter'], prefix='exp_fe')  # repeat for exporters
exporter_fixed_effects = exporter_fixed_effects.drop('exp_fe_ZAF', axis=1)  # drop a column to avoid collinearity

# Split the data into right side and left side variables
lhs_data = estimation_data[['log_trade']]
rhs_data = estimation_data[['log_distance', 'contiguity', 'agree_pta', 'common_language']]

# Add the dummies to the right hand variables
rhs_data = pd.concat(objs=[rhs_data, importer_fixed_effects, exporter_fixed_effects], axis=1)  # concatinate
# is a method of combining two datasets that does not rely on merging/joining on keys, it does so on rows or columns
# 'objs' is a list of DataFrames to concatinate (they need to have the same row or column IDs as each other)
# 'axis' specifies whether you want to concatinate rows or colomns. axis = 1 specifies that the columns are to be
# combined (i.e. horizontal combining)
rhs_data.columns





####################
# Step 5: Estimation
####################
ols_model = sm.OLS(lhs_data, rhs_data)  # This step is a little odd. It creates a python "regression object", to which
# various other OLS fuctions can be applied
ols_results = ols_model.fit()  # .fit() is probably the most important function as it returns an object with
#  the estimated results.
ols_results.summary()  # returns the results in a standard format
ols_results.params  # returns only the parameter values
ols_results.rsquared  # The r squared values
ols_results.HC1_se  # Huber/White standard errors. You could also return this from the getgo with
# ols_model.fit(cov_type = 'HC1')
ols_results.pvalues  # pvalues





###########
# Step 6: Saving the results
###########
# To write the results to a text file, you need to 'open' a text file on the hard drive, write the results to the file,
# and close the file
text_file = open(
    "C:\\Documents\\regression_results.txt", "w")
text_file.write(ols_results.summary().as_text())
text_file.close()

# Alternatively, you could export some of these results to excel
type(ols_results.params)  # Statsmodels conveniently returns Pandas Objects, so we can feed them into a dataframe
results_dataframe = pd.concat(
    {'coefficients': ols_results.params, 'SE': ols_results.HC1_se, 'p_values': ols_results.pvalues}, axis=1)
results_dataframe.head(5)
results_dataframe.to_csv(
    "C:\\Documents\\regression_results.csv")

