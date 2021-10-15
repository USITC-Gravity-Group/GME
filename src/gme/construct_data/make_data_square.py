__Author__ = "Peter Herman"
__Project__ = "Construct Data"
__Created__ = "01/11/2018"
__all__ = ['make_data_square']

import numpy as np
import pandas as pd
from warnings import warn


def make_data_square(trade_dataframe=None,
                     imp_var_name: str = "importer",
                     exp_var_name: str = "exporter",
                     multiple_sectors: bool = False,
                     sector_var_name: str = None,
                     year_var_name: str = "year",
                     drop_intratrade: bool = True,
                     year_by_year: bool = True):
    """
    Expand countries and sectors by adding zero-valued trade flows to make the panel square.
    Args:
        trade_dataframe: pd.DataFrame
            A DataFrame containing trade values and observation identifiers (importer, exporter, year, and (optionally)
            sector).
        imp_var_name: str
            The name of the column containing importer identifiers.
        exp_var_name: str
            The name of the column containing exporter identifiers.
        multiple_sectors: bool
            If true, the data is squared for each sector as well. Default is False.
        sector_var_name: (optional) str
            The name of the column containing sector identifiers. Must be supplied if squaring for each section (i.e.
            if multiple_sectors = True).
        year_var_name: (optional) str
            The name of the column containing year identifiers.
        drop_intratrade: bool
            If True, the returned data will not contain intranational observations in which the importer and exporter
            are the same country. Default is True.
        year_by_year: bool
            If true, the data is squared on a year by year basis, which allows the dimensions to differ each year. For
            example, it lets the set of countries or sectors around which the data is squared to differ each year.
            Doing so reduces the likelihood of including countries or sectors with zero trade activity in certain years.

    Returns: pd.DataFrame
        A square dataset.

    """
    if (multiple_sectors and sector_var_name is None):
        raise ValueError("A column name for sectors is required if multiple_sectors == True")

    if not year_by_year:
        complete_square_data = _not_year_by_year(trade_dataframe, imp_var_name, exp_var_name,
                                                 multiple_sectors, sector_var_name, year_var_name, drop_intratrade)

    else:
        complete_square_data = _year_by_year(trade_dataframe,
                                             imp_var_name,
                                             exp_var_name,
                                             multiple_sectors,
                                             sector_var_name,
                                             year_var_name,
                                             drop_intratrade)

    return complete_square_data


def _not_year_by_year(trade_dataframe,
                      importer_var_name: str,
                      exporter_var_name: str,
                      multiple_sectors: bool,
                      sector_var_name: str,
                      year_var_name: str,
                      drop_intratrade: bool):
    '''
    Creates a square dataset based on observation present in any year.
    :param trade_dataframe: (Pandas DataFrame) A Pandas DataFrame containing bilateral trade data
    :param importer_var_name: (str) The name of the column containing importer IDs.
    :param exporter_var_name: (str) The name of the column containing exporter IDs.
    :param multiple_sectors: (bool) True if the data contains multiple sectors. Default is False.
    :param sector_var_name: (str) The name of the column containing sector IDs, if applicable.
    :param year_var_name: (str) The name of the column containing year IDs, if applicable
    :param drop_intratrade: (bool) True if you would like intra-country observations dropped (i.e. importer == exporter). Default is True
    :return: a square (Pandas DataFrame) object
    '''
    countries = _country_list(trade_dataframe, importer_var_name, exporter_var_name)
    countries['key'] = 0  # this provides a series to merge on.

    square_data = countries.merge(countries, how='outer', on='key')
    square_data.rename(index=str, columns={"0_x": importer_var_name, "0_y": exporter_var_name}, inplace=True)

    merging_dimensions = [importer_var_name, exporter_var_name]
    expected_length = len(countries)
    expected_width = 3

    if multiple_sectors:
        square_data, merging_dimensions, expected_length, expected_width = _square_multiple_sectors(trade_dataframe,
                                                                                                    sector_var_name,
                                                                                                    merging_dimensions,
                                                                                                    expected_length,
                                                                                                    expected_width)

    square_data, merging_dimensions, expected_length, expected_width = _square_years(trade_dataframe, square_data,
                                                                                     year_var_name, merging_dimensions,
                                                                                     expected_length, expected_width)

    if drop_intratrade:
        square_data = _drop_intratrade(square_data, importer_var_name, exporter_var_name)
        expected_length = expected_length * (len(countries) - 1)
    else:
        expected_length = expected_length * len(countries)

    square_data.drop('key', axis=1, inplace=True)
    square_data = square_data.merge(trade_dataframe, how='left', on=merging_dimensions)
    square_data.fillna(0, inplace=True)

    if square_data.shape != (expected_length, expected_width):
        warn(
            "dimensions of the constructed square data ({0}, {1}) do not match the expected dimensions ({2}, {3})".format(
                square_data.shape[0], square_data.shape[1], expected_length, expected_width))

    print("Number of Missing Values in Square Trade Data")
    print(square_data.isnull().sum())

    complete_square_data = square_data

    return complete_square_data


def _year_by_year(trade_dataframe,
                  importer_var_name: str,
                  exporter_var_name: str,
                  multiple_sectors: bool,
                  sector_var_name: str,
                  year_var_name: str,
                  drop_intratrade: bool):
    '''
    Creates a square dataset such that each year is squared based on the observations present only in that year.
    :param trade_dataframe: (Pandas DataFrame) A Pandas DataFrame containing bilateral trade data
    :param importer_var_name: (str) The name of the column containing importer IDs.
    :param exporter_var_name: (str) The name of the column containing exporter IDs.
    :param multiple_sectors: (bool) True if the data contains multiple sectors. Default is False.
    :param sector_var_name: (str) The name of the column containing sector IDs, if applicable.
    :param year_var_name: (str) The name of the column containing year IDs, if applicable
    :param drop_intratrade: (bool) True if you would like intra-country observations dropped (i.e. importer == exporter). Default is True
    :return: a square (Pandas DataFrame) object
    '''
    years = _year_list(trade_dataframe, year_var_name)
    grouped_data = trade_dataframe.groupby(year_var_name)
    iteration_counter = 1

    for year_group in years:
        print(year_group)

        year_data = grouped_data.get_group(year_group)
        countries = _country_list(year_data, importer_var_name, exporter_var_name)

        print("Number of Countries in " + str(year_group) + ': ' + str(len(countries)))
        countries['key'] = 0  # this provides a series to merge on.

        square_data = countries.merge(countries, how='outer', on='key')
        square_data.rename(index=str, columns={"0_x": importer_var_name, "0_y": exporter_var_name}, inplace=True)

        merging_dimensions = [importer_var_name, exporter_var_name, year_var_name]
        expected_length = len(countries)
        expected_width = 3

        if multiple_sectors:
            square_data, merging_dimensions, expected_length, expected_width = _square_multiple_sectors(year_data,
                                                                                                        square_data,
                                                                                                        sector_var_name,
                                                                                                        merging_dimensions,
                                                                                                        expected_length,
                                                                                                        expected_width)

        square_data[year_var_name] = int(year_group)
        expected_width += 1

        if drop_intratrade:
            square_data = _drop_intratrade(square_data, importer_var_name, exporter_var_name)
            expected_length = expected_length * (len(countries) - 1)
        else:
            expected_length = expected_length * len(countries)

        square_data.drop('key', axis=1, inplace=True)

        square_data = square_data.merge(year_data, how='left', on=merging_dimensions)
        square_data.fillna(0, inplace=True)

        if square_data.shape != (expected_length, expected_width):
            warn(
                "dimensions of the constructed square data ({0}, {1}) do not match the expected dimensions ({2}, {3})".format(
                    square_data.shape[0], square_data.shape[1], expected_length, expected_width))

        print("Number of Missing Values in Square Trade Data")
        print(square_data.isnull().sum())

        if iteration_counter == 1:
            complete_square_data = square_data
        else:
            complete_square_data = complete_square_data.append(square_data)
        iteration_counter += 1

    return complete_square_data


def _year_list(dataframe, year_var_name):
    '''
    Create a list of years in the data
    :param dataframe:(Pandas DataFrame) dataframe to extract years from
    :param year_var_name: (str) name of column containing year IDs
    :return: a list of years in the data
    '''
    years = pd.DataFrame(dataframe[year_var_name].unique())
    return years[0].tolist()


def _country_list(dataframe, importer_var_name, exporter_var_name):
    '''
    Create a list of importers and exporters in the data
    :param dataframe: (Pandas DataFrame) dataframe to extract countries from
    :param importer_var_name: (str) name of column containing importer IDs
    :param exporter_var_name: (str) name of column containing exporter IDs
    :return: a list of all countries in the data
    '''
    countries = np.concatenate((dataframe[importer_var_name].unique(), dataframe[exporter_var_name].unique()),
                               axis=0)
    return pd.DataFrame(pd.DataFrame(countries)[0].unique())


def _square_multiple_sectors(original_dataframe, square_dataframe, sector_var_name, merging_dimensions, expected_length,
                             expected_width):
    '''
    Squares a dataframe along the 'sectors' dimension.
    :param original_dataframe: (Pandas DataFrame) Dataframe to extract a sector list from
    :param square_dataframe: (Pandas DataFrame) Square dataframe to expand to sectors
    :param sector_var_name: (str) name of column containing sector IDs
    :param merging_dimensions: (List) A list containing the column names to merge observed data back onto
    :param expected_length: (int) expected number of rows in square_dataframe
    :param expected_width: (int) expected number of columns in square_dataframe
    :return: square_dataframe - (Pandas Dataframe)  updated version of input square_dataframe with sectors squared too.
             merging_dimensions - (List) updated...
             expected_length - (int) updated...
             expected_width - *int) updated...
    '''
    sectors = pd.DataFrame(original_dataframe[sector_var_name].unique())
    sectors['key'] = 0
    square_dataframe = square_dataframe.merge(sectors, how='outer', on='key')
    square_dataframe.rename(index=str, columns={0: sector_var_name}, inplace=True)
    merging_dimensions.append(sector_var_name)
    expected_length = expected_length * len(sectors)
    expected_width += 1
    return square_dataframe, merging_dimensions, expected_length, expected_width


def _square_years(original_dataframe, square_dataframe, year_var_name, merging_dimensions, expected_length,
                  expected_width):
    '''
    Sqaures a dataframe along the 'years' dimension.
    :param original_dataframe: (Pandas DataFrame) Dataframe to extract a year list from
    :param square_dataframe: (Pandas DataFrame) Square dataframe to expand to years
    :param year_var_name: (str) name of column containing year IDs
    :param merging_dimensions: (List) A list containing the column names to merge observed data back onto
    :param expected_length: (int) expected number of rows in square_dataframe
    :param expected_width: (int) expected number of columns in square_dataframe
    :return: square_dataframe - (Pandas Dataframe)  updated version of input square_dataframe with years squared too.
             merging_dimensions - (List) updated...
             expected_length - (int) updated...
             expected_width - *int) updated...
    '''
    years = pd.DataFrame(original_dataframe[year_var_name].unique())
    years['key'] = 0
    square_dataframe = square_dataframe.merge(years, how='outer', on='key')
    square_dataframe.rename(index=str, columns={0: year_var_name}, inplace=True)
    merging_dimensions.append(year_var_name)
    expected_length = expected_length * len(years)
    expected_width += 1
    return square_dataframe, merging_dimensions, expected_length, expected_width


def _drop_intratrade(dataframe,
                     importer_var_name,
                     exporter_var_name):
    '''
    Drops intratrade observations (i.e. importer == exporter)
    :param dataframe: (Pandas DataFrame)
    :param importer_var_name: (str) The name of the column containing importer IDs.
    :param exporter_var_name: (str) The name of the column containing exporter IDs.
    :return: (Pandas DataFrame)
    '''
    dataframe.drop(
        dataframe.loc[dataframe[importer_var_name] == dataframe[exporter_var_name]].index,
        inplace=True)
    return dataframe
