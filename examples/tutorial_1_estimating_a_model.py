
import pandas as pd
from src.gme.construct_data import EstimationData
from src.gme.estimate.EstimationModel import EstimationModel

gravity_data = pd.read_csv('https://www.usitc.gov/data/gravity/example_trade_and_grav_data_small.csv')

gravity_data.head()

gme_data = EstimationData(data_frame=gravity_data,
                          imp_var_name='importer',
                          exp_var_name='exporter',
                          trade_var_name='trade_value',
                          year_var_name='year',
                          notes='Downloaded from https://www.usitc.gov/data/gravity/example_trade_and_grav_data_small.csv')

gme_data

gme_data.number_of_importers
gme_data.columns
gme_data.year_list()
country_list = gme_data.countries_each_year()
country_list[1989]


gme_data.dtypes()
gme_data.info()
gme_data.describe()


gme_data.data_frame['trade_value']

aggregated_data_1 = gme_data.tabulate_by_group(tab_variables = ['trade_value','log_distance'],
                                               by_group = ['importer'],
                                               how = ['mean','min','max'])
aggregated_data_1.head(5)

aggregated_data_2 = gme_data.tabulate_by_group(tab_variables = ['trade_value'],
                                               by_group = ['importer','exporter'],
                                               how = ['mean','std', 'count'])
aggregated_data_2.head(5)


model_baseline = EstimationModel(estimation_data= gme_data,
                                 lhs_var = 'trade_value',
                                 rhs_var = ['log_distance','agree_pta',
                                            'common_language','contiguity'])
model_baseline.estimate()
print(model_baseline.results_dict['all'].summary())

fixed_effects_model  = EstimationModel(estimation_data= gme_data,
                                       lhs_var = 'trade_value',
                                       rhs_var = ['log_distance','agree_pta',
                                            'common_language','contiguity'],
                                       fixed_effects=[['importer','year'],
                                                ['exporter','year']])

data_subset_model = EstimationModel(estimation_data= gme_data,
                                    lhs_var = 'trade_value',
                                    rhs_var = ['log_distance','agree_pta',
                                            'common_language','contiguity'],
                                    drop_imp_exp=['USA'],
                                    keep_years=[2015, 2014, 2013])


fixed_effects_model_2  = EstimationModel(estimation_data= gme_data,
                                         lhs_var = 'trade_value',
                                         rhs_var = ['log_distance','agree_pta',
                                            'common_language','contiguity'],
                                         fixed_effects=[['importer','year'],
                                                ['exporter','year']],
                                         keep_years=[2013,2014,2015])
model_baseline.estimate()
print(model_baseline.results_dict['all'].summary())

estimates = fixed_effects_model_2.estimate()

estimates.keys()

results = estimates['all']
results.summary()

coefficients = results.params
coefficients.head()

results.bse
results.pvalues

results.fittedvalues

fixed_effects_model_2.ppml_diagnostics
fixed_effects_model_2.ppml_diagnostics['Perfectly Collinear Variables']


combined_results = fixed_effects_model_2.combine_sector_results()
combined_results.head()

fixed_effects_model_2.format_regression_table(format='csv',
                                            se_below = True,
                                            omit_fe_prefix = ['importer_year',
                                                                   'exporter_year'])