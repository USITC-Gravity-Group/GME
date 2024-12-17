__Author__ = "Peter Herman"
__Project__ = "GE Gravity"
__Created__ = "02/20/2018"
__all__ = ['EstimationData']
import numpy as np
import pandas as pd
from .DataLog import DataLog
from typing import List
import matplotlib.pyplot as plt


class EstimationData(object):
    def __init__(self,
                 data_frame=None,
                 name: str = 'unnamed',
                 imp_var_name: str = 'importer',
                 exp_var_name: str = 'exporter',
                 year_var_name: str = 'year',
                 trade_var_name: str = None,
                 sector_var_name: str = None,
                 expend_var_name: str = None,
                 output_var_name: str = None,
                 notes: List[str] = list()):
        '''
        An object used for storing data for gravity modeling and producing some summary statistics.
        Args:
            data_frame: Pandas.DataFrame
                A DataFrame containing trade, gravity, etc. data.
            name: (optional) str
                A name for the dataset.
            imp_var_name: str
                The name of the column containing importer IDs.
            exp_var_name: str
                The name of the column containing exporter IDs.
            year_var_name: str
                The name of the column containing year data.
            trade_var_name: (optional) str
                The name of the column containing trade data.
            sector_var_name: (optional) str
                The name of the column containing sector/industry/product IDs.
            expend_var_name: (optional) str
                The name of the column containing importer total expenditure information.
            output_var_name: (optional) str
                The name of the column containing exporter total output information
            notes: (optional) str
                A string to be included as a note n the object.

        Attributes:
            data_frame: Pandas.DataFrame
                The supplied DataFrame.
            name: str
                The supplied data name.
            imp_var_name: str
                The name of the column containing importer IDs.
            exp_var_name: str
                The name of the column containing exporter IDs.
            year_var_name: str
                The name of the column containing year data.
            trade_var_name: str
                The name of the column containing trade data.
            sector_var_name: str
                The name of the column containing sector/industry/product IDs.
            notes: List[str]
                A list of notes.
            number_of_exporters: int
                The number of unique exporter IDs in the dataset.
            number_of_importers: int
                The number of unique importer IDs in the dataset.
            shape: List[int]
                The dimensions of the dataset.
            countries: List[str]
                A list of the unique country IDs in the dataset.
            number_of_countries: int
                The number of unique country IDs in the dataset.
            number_of_years: int
                The number of years in the dataset
            columns: List[str]
                A list of column names in the dataset.
            number_of_sectors: int
                If a sector is specified, the number of unique sector IDs in the dataset.

        Methods:
            tablulate_by_group:
                Summarize columns by a user-specified grouping. Can be used to tabulate, aggregate, summarize,
                etc. data.

                Args:
                    tab_variables: List[str]
                        Column names of variables to be tabulated
                    by_group: List[str]
                        Column names of variables by which to group observations for tabulation.
                    how: List[str]
                        The method by which to combine observations within a group. Can accept 'count','mean',
                        'median','min','max','sum','prod','std', and 'var'. It may work with other numpy or
                        pandas functions.

                Returns: Pandas.DataFrame
                    A DataFrame of tabulated values for each group.

            year_list:
                Returns a list of years present in the data
                Args:
                    none
                Returns: list

            countries_each_year
                Returns a dictionary keyed by year ID containing a list of country IDs present in each corresponding
                year.
                Args:
                    none
                Returns: dict

            sector_list
                Returns a list of unique sector IDs

            dtypes:
                Returns the data types of the columns in the DataObject.data_frame using Pandas.DataFrame.dtypes().
                See Pandas documentation for more information.
                Examples:

            info:
                Print summary information about DataObject.data_frame using Pandas.DataFrame.dtypes(). See Pandas
                documentation for more information.

            describe:
                Generates some descriptive statistics for DataObject.data_frame using Pandas.DataFrame.describe().
                See Pandas documentation for more information.

            add_note:
                Add a note to the list of notes in 'notes' attribute.
                Args:
                     note: str
                        A note to add to DataObject.
                Returns: none

            correlation:
                Return and plot the correlation matrix of the data.
                Args:
                    columns: List[str] (optional)
                        A list of column names to include in the matrix. Default is to include all columns.
                    plot: bool
                        If True, it plots a heatmap of the correlation matrix.
                Returns: Pandas.DataFrame
                    A correlation matrix

            add_pair_var:
                Create a new variable that is a concatenation of categorical variables for use as a fixed effect or
                cluster category, for example. Original values are separated by '_' in the concatenated value.
                Args:
                    var_list: List[str]
                        List of names of columns to concatinate.
                    var_name: (Optional) str
                        Column name to use for the new variable. By default, it uses the names in var_list separated by
                        '_'.
                    symmetric: bool
                        If False, all variables are concatenated in the order of the var_list (e.g. ARG_USA
                        and USA_ARG would both would be created). If True, ignores ordering of values across columns and
                        concatenates alphabetically (e.g. all ARG and USA pairings would concatenate as ARG_USA)

                Returns: None, adds new column to EstimationData.dataframe.


        Examples:
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

            # Create a DataObject
            example_data_object = DataObject(data_frame=gravity_data,
                                             imp_var_name='importer',
                                             exp_var_name='exporter',
                                             trade_var_name='trade_value',
                                             year_var_name='year',
                                             notes='Downloaded from https://www.usitc.gov/data/gravity/example_trade_and_grav_data_small.csv')

            # tabulate_by_group
            # Sum trade value by importer and year
            >>> aggregated_data = example_data_object.tabulate_by_group(tab_variables = ['trade_value'],
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
            >>> summarized_data = example_data_object.tabulate_by_group(tab_variables = ['trade_value'],
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
            >>> example_data_object.year_list()
            [1989,
             1990,
             1991,
             1992,
             ...

            # countries_each_year
            >>> countries = example_data_object.countries_each_year()
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
            >>> example_data_object.dtypes()
            importer            object
            exporter            object
            year                 int64
            trade_value        float64
            agree_pta          float64
            common_language    float64
            contiguity         float64
            log_distance       float64
            dtype: object

            >>> example_data_object.info()
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
            >>> example_data_object.describe()
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
            >>> example_data_object.add_note('year IDs are integers')
            >>> example_data_object.notes
            ['Downloaded from https://www.usitc.gov/data/gravity/example_trade_and_grav_data_small.csv',
            'year IDs are integers']


        '''

        ##############
        # Attributes #
        ##############
        self.data_frame = data_frame.copy()
        self.name = name
        self.imp_var_name = imp_var_name
        self.exp_var_name = exp_var_name
        self.year_var_name = year_var_name
        self.trade_var_name = trade_var_name
        self.sector_var_name = sector_var_name
        self.expend_var_name = expend_var_name
        self.output_var_name = output_var_name
        self.notes = [notes]
        self.number_of_exporters = len(data_frame[exp_var_name].unique())
        self.number_of_importers = len(data_frame[imp_var_name].unique())
        self.shape = self.data_frame.shape

        countries = np.concatenate((data_frame[imp_var_name].unique(), data_frame[exp_var_name].unique()),
                                   axis=0)
        countries = pd.DataFrame(pd.DataFrame(countries)[0].unique())
        self.countries = list(countries)
        self.number_of_countries = len(countries)

        self.number_of_years = len(data_frame[year_var_name].unique())
        self.columns = list(self.data_frame.columns.values)
        if sector_var_name is not None:
            self.number_of_sectors = len(data_frame[sector_var_name].unique())
        else:
            self.number_of_sectors = 'not_applicable'

        self.data_log = DataLog()  # Add initialization values as needed

        self.meta_data = _MetaData(imp_var_name=self.imp_var_name,
                                   exp_var_name=self.exp_var_name,
                                   year_var_name=self.year_var_name,
                                   trade_var_name=self.trade_var_name,
                                   sector_var_name=self.sector_var_name,
                                   expend_var_name=self.expend_var_name,
                                   output_var_name=self.output_var_name)

    ###########
    # Methods #
    ###########
    def tabulate_by_group(self, tab_variables: list, by_group: list, how: list):
        '''
        Creates summary stats by group.
        Args:
            tab_variables: List[str]
                A list of column names to tabulate/aggregate
            by_group: List[str]
                A list of column names by which to group the tabulation/aggregation
            how: List[str]
                A list of methods to apply to each tabulated variable. Can be selected from 'count', 'mean','median',
                'min','max','sum','prod','std',or 'var'. It may work with other numpy or pandas functions.
        Returns: Pandas DataFrame
            Tabulated/aggregated results,
        '''
        tabulate_data = self.data_frame[tab_variables + by_group]
        # IDEA: it would be possible to do a version in which a lambda function is fed that can create custom summary stats
        if by_group != []:
            tabulate_data = tabulate_data.groupby(by_group).agg(how).reset_index()
            # The following combines the auto-generated, hierarchic column names into a single name
            tabulate_data.columns = ['_'.join(col).strip() for col in tabulate_data.columns.values]
        else:
            tabulate_data = tabulate_data.agg(how).reset_index()
        return tabulate_data

    def dtypes(self):
        return self.data_frame.dtypes

    def info(self):
        return self.data_frame.info()

    def describe(self):
        return self.data_frame.describe()

    def year_list(self):
        '''
        A function that returns a list of the years present in the dataframe
        Returns: list
            A list of years
        '''
        return list(self.data_frame[self.year_var_name].unique())

    def countries_each_year(self):
        '''
        A function to create a collection of countries present in each year of the data.
        Returns: dict
            A dictionary in which each dictionary entry corresponds to a year and features a (list) of countries.
            i.e. {year:country_list}. For example: return_object[year] returns a list of countries in that year
        '''
        country_dict = {}
        year_list = list(self.data_frame[self.year_var_name].unique())
        for year in year_list:
            year_data = self.data_frame.loc[self.data_frame[self.year_var_name] == year]
            importers = list(year_data[self.imp_var_name].unique())
            exporters = list(year_data[self.exp_var_name].unique())
            countries = set().union(importers, exporters)
            countries = list(countries)
            country_dict[year] = countries
        return country_dict
    
    
    def sector_list(self):
        return list(self.data_frame[self.sector_var_name].unique())

    def _extract_meta_data(self):
        '''
        Function to collect and assign meta data from data_summary object
        Returns: str
            Column names for importer, exporter, year, and sector fields
        '''
        return self.imp_var_name, self.exp_var_name, self.year_var_name, self.sector_var_name

    def add_note(self, note: str):
        '''
        Add a note to the 'notes' attribute
        Args:
            note: str
                A string to add to the list of notes
        Returns: None
        '''
        self.notes.append(note)

    def correlation(self, columns: List[str] = None, plot: bool = False):
        '''
        Return and plot the correlation matrix of the data.
        Args:
            columns: List[str] (optional)
                A list of column names to include in the matrix. Default is to include all columns.
            plot: bool
                If True, it plots a heatmap of the correlation matrix.

        Returns: Pandas.DataFrame
            A the correlation matrix
        '''
        if columns is None:
            corr_mat = self.data_frame.corr()
        else:
            corr_mat = self.data_frame[columns].corr()
        # Plot Correlation Matrix
        if plot:
            fig = plt.figure()
            ax = fig.add_subplot(111)
            cax = ax.matshow(corr_mat, interpolation='nearest', cmap = 'PiYG')
            fig.colorbar(cax)
            labels = list(corr_mat.columns.values)
            ax.set_xticks(np.arange(len(labels)))
            ax.set_yticks(np.arange(len(labels)))
            ax.set_xticklabels(labels, rotation='vertical')
            ax.set_yticklabels(labels)
            plt.show()
        return corr_mat

    def add_pair_var(self, var_list: List[str] = [], var_name: str = '', symmetric: bool = False):
        '''
        Create a new variable that is a concatenation of categorical variables for use as a fixed effect or cluster
        category, for example. Original values are separated by '_' in the concatenated value.
        Args:
            var_list: List[str]
                List of names of columns to concatinate.
            var_name: (Optional) str
                Column name to use for the new variable. By default, it uses the names in var_list separated by '_'.
            symmetric: bool
                If False, all variables are concatenated in the order of the var_list (e.g. ARG_USA
                and USA_ARG would both would be created). If True, ignores ordering of values across columns and
                concatenates alphabetically (e.g. all ARG and USA pairings would concatenate as ARG_USA)

        Returns: None, adds new column to EstimationData.dataframe.
        '''
        if len(var_name)==0:
            var_name = '_'.join(var_list)
        temp_data_frame = self.data_frame.loc[:, var_list].copy()
        for col in var_list:
            temp_data_frame[col] = temp_data_frame[col].astype(str)
        if symmetric:
            self.data_frame[var_name] = ['_'.join(x) for x in np.sort(temp_data_frame, axis=1)]
        else:
            self.data_frame[var_name] = temp_data_frame.apply('_'.join,axis=1)

        return None

    def __repr__(self):
         return "number of countries: {0} \n" \
                "number of exporters: {1} \n" \
                "number of importers: {2} \n" \
                "number of years: {3} \n" \
                "number of sectors: {4} \n" \
                "dimensions: {5}\n" \
             .format(self.number_of_countries,
                     self.number_of_exporters,
                     self.number_of_importers,
                     self.number_of_years,
                     self.number_of_sectors,
                     self.shape)










class _MetaData(object):
    '''
    A class that contains certain information to simplify its passing around different estimate routines.
    '''

    def __init__(self,
                 imp_var_name: str = 'importer',
                 exp_var_name: str = 'exporter',
                 year_var_name: str = 'year',
                 trade_var_name: str = None,
                 sector_var_name: str = None,
                 expend_var_name: str = None,
                 output_var_name: str = None,
                 ):
        self.imp_var_name = imp_var_name
        self.exp_var_name = exp_var_name
        self.year_var_name = year_var_name
        self.trade_var_name = trade_var_name
        self.sector_var_name = sector_var_name
        self.expend_var_name = expend_var_name
        self.output_var_name = output_var_name

    def __repr__(self):
        return "imp_var_name: {0} \n" \
               "exp_var_name: {1} \n" \
               "year_var_name: {2} \n" \
               "trade_var_name: {3} \n" \
               "sector_var_name: {4} \n" \
               "expend_var_name: {5}\n" \
               "output_var_name: {6} \n" \
            .format(self.imp_var_name,
                    self.exp_var_name,
                    self.year_var_name,
                    self.trade_var_name,
                    self.sector_var_name,
                    self.expend_var_name,
                    self.output_var_name)
