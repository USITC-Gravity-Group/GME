__Author__ = "Peter Herman"
__Project__ = "Gravity Code"
__Created__ = "06/03/2020"
__Description__ = "Testing and demonstration of new features in version 1.3 release."

import pandas as pd
from src.gme.construct_data.EstimationData import EstimationData
from src.gme.construct_data.make_data_square import make_data_square
from src.gme.estimate.EstimationModel import EstimationModel
from src.gme.estimate.format_regression_table import format_regression_table

raw_data = pd.read_csv(
    "https://www.usitc.gov/data/gravity/example_trade_and_grav_data_small.csv")

grav_vars = ['agree_pta', 'common_language', 'contiguity', 'log_distance']

# -----
# Test data features
# -----

# Make data square
trade_data = raw_data[['importer', 'exporter', 'year', 'trade_value']].copy()
# square_data = make_data_square(trade_data, imp_var_name='importer', exp_var_name='exporter',
#                                multiple_sectors=False,  year_var_name='year',
#                                drop_intratrade=False, year_by_year=True)

est_data = EstimationData(raw_data, imp_var_name='importer', expend_var_name='exporter', year_var_name='year')
est_data.add_pair_var(var_list=['importer', 'exporter'], var_name='bilat_pair', symmetric=True)

# Correlation Table
corr_table = est_data.correlation(columns=['trade_value']+grav_vars, plot=True)

# ---
# Test Estimation
# ---
compare_regs = dict()

# Baseline Model using old features
est_model_1 = EstimationModel(est_data,
                              lhs_var='trade_value',
                              rhs_var=grav_vars,
                              sector_by_sector=False,
                              fixed_effects=[['importer', 'year'], ['exporter', 'year']])
est_model_1.estimate()

# Check for identifiers on modefied data
mod_data = est_model_1.modified_data['all']

compare_regs['(Baseline)'] = est_model_1.results_dict['all']
table_1 = est_model_1.format_regression_table()

# Demo Omit Fixed Effects
est_model_2 = EstimationModel(est_data,
                              lhs_var='trade_value',
                              rhs_var=grav_vars,
                              fixed_effects=[['importer', 'year'], ['exporter', 'year']],
                              omit_fixed_effect={'importer': ['DEU', 'DNK']})
est_model_2.estimate()
compare_regs['(Omit FE 1)'] = est_model_2.results_dict['all']

# Demo more specific fixed effect dropping (must be tuples)
est_model_3 = EstimationModel(est_data,
                              lhs_var='trade_value',
                              rhs_var=grav_vars,
                              fixed_effects=[['importer', 'year'], ['exporter', 'year']],
                              omit_fixed_effect={('importer', 'year'): [('DEU', '2015')], 'exporter': ['USA']})
est_model_3.estimate()
compare_regs['(Omit FE 2)'] = est_model_3.results_dict['all']

# Test Cluster Option
est_model_4 = EstimationModel(est_data,
                              lhs_var='trade_value',
                              rhs_var=grav_vars,
                              fixed_effects=[['importer', 'year'], ['exporter', 'year']],
                              cluster_on='bilat_pair')
est_model_4.estimate()
compare_regs['(cluster)'] = est_model_4.results_dict['all']
hold = est_model_4.results_dict['all']

reg_table = format_regression_table(compare_regs, note="Table of regressions demonstrating new features")
