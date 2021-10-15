## Function
gme.<strong>make_data_square</strong>(<em>trade_dataframe=None,
                     imp_var_name: str = "importer",
                     exp_var_name: str = "exporter",
                     multiple_sectors: bool = False,
                     sector_var_name: str = None,
                     year_var_name: str = "year",
                     drop_intratrade: bool = True,
                     year_by_year: bool = True</em>):
                     
## Description
Expand countries and sectors by adding zero-valued trade flows to make the panel square.

## Arguments
<dl>
<dt> <strong>trade_dataframe</strong>: <em>pd.DataFrame</em></dt>
<dd><p>A DataFrame containing trade values and observation identifiers (importer, exporter, year, and (optionally) sector). </p></dd>
</dl>


<dt> 
<strong>imp_var_name</strong>: str</dt>
 <dd><p>The name of the column containing importer identifiers.</p></dd>


<dt> <strong>exp_var_name</strong>: <em>str</em></dt>
 <dd><p>The name of the column containing exporter identifiers.</p></dd>

<dl>
<dt> <strong>multiple_sectors</strong>: <em>bool</em></dt>
 <dd><p>If true, the data is squared for each sector as well. Default is False.</p></dd>


<dt> <strong>sector_var_name</strong>: <em>(optional) str</em></dt>
<dd><p> The name of the column containing sector identifiers. Must be supplied if squaring for each section (i.e. if multiple_sectors = True).</p></dd>


<dt> <strong>year_var_name</strong>: <em>(optional) str</em> </dt>
 <dd><p>The name of the column containing year identifiers.</p></dd>


<dt> <strong>drop_intratrade</strong>: <em>bool</em></dt>
 <dd><p>If True, the returned data will not contain intranational observations in which the importer and exporter are the same country. Default is True.</p></dd>


<dt> <strong>year_by_year</strong>: <em>bool</em></dt>
<dd><p>If true, the data is squared on a year by year basis, which allows the dimensions to differ each year. For example, it lets the set of countries or sectors around which the data is squared to differ each year. Doing so reduces the likelihood of including countries or sectors with zero trade activity in certain years.</p></dd>

## Returns
<strong>Returns</strong>: <em>Pandas.DataFrame</em>
 A square dataset.

## Examples
```python
>>> raw_data =  pd.read_csv('https://www.usitc.gov/data/gravity/example_trade_and_grav_data_small.csv')
>>> trade_data = raw_data[['importer', 'exporter', 'year', 'trade_value']]
>>> square_data = make_data_square(trade_data, imp_var_name='importer', exp_var_name='exporter',
                                multiple_sectors=False, year_var_name='year',
                                drop_intratrade=False, year_by_year=True)
```