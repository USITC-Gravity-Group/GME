__Author__ = "Peter Herman"
__Project__ = "gme.estimate"
__Created__ = "03/28/2018"

'''
data_frame = estimation_test.estimation_data.data_frame
specification = estimation_test.specification
data_log = estimation_test.estimation_data.data_log
meta_data = estimation_test.estimation_data._meta_data

'''



def _slice_data_for_estimation(data_frame,
                               specification,
                               meta_data,
                               data_log):

    # Keep Only Using Variables
    data_frame, data_log = _keep_using_vars(data_frame, specification, meta_data, data_log)

    # Drop intra-trade
    data_frame, data_log =_drop_intra_trade(data_frame, specification, meta_data, data_log)

    # Drop Importers
    data_frame, data_log = _drop_importers(data_frame, specification, meta_data, data_log)

    # Drop Exporters
    data_frame, data_log = _drop_exporters(data_frame, specification, meta_data, data_log)

    # Keep importers
    data_frame, data_log = _keep_importers(data_frame, specification, meta_data, data_log)

    # Keep Exporters
    data_frame, data_log = _keep_exporters(data_frame, specification, meta_data, data_log)

    # Drop Years
    data_frame, data_log = _drop_years(data_frame, specification, meta_data, data_log)

    # Keep Years
    data_frame, data_log = _keep_years(data_frame, specification, meta_data, data_log)

    # Drop Missing
    data_frame, data_log = _drop_missing(data_frame, specification, data_log)

    return data_frame, data_log



#---------------
# Sub-routines
#---------------

def _keep_using_vars(data_frame,
                               specification,
                               meta_data,
                               data_log):
    pre_drop_size = data_frame.shape
    using_variables = specification.rhs_var+[specification.lhs_var, meta_data.imp_var_name, meta_data.exp_var_name,
                                             meta_data.year_var_name]
    if meta_data.sector_var_name is not None:
        using_variables = using_variables + [meta_data.sector_var_name]
    data_frame = data_frame[using_variables]
    post_drop_size = data_frame.shape
    dropped_dims = {'rows': pre_drop_size[0] - post_drop_size[0], 'columns': pre_drop_size[1] - post_drop_size[1]}
    data_log.specification_variables_kept = str(using_variables) + ', Observations excluded by user: ' + str(dropped_dims)
    if specification.verbose is True:
        print('select specification variables: ' + data_log.specification_variables_kept)
    return data_frame, data_log

def _drop_intra_trade(data_frame,
                     specification,
                     meta_data,
                     data_log):
    pre_drop_size = data_frame.shape
    if specification.drop_intratrade is True:
        data_frame = data_frame[data_frame[meta_data.imp_var_name] != data_frame[meta_data.exp_var_name]].copy()
        data_log.intra_country_trade_dropped = 'yes'
    else:
        data_log.intra_country_trade_dropped = 'no'
    post_drop_size = data_frame.shape
    dropped_dims = {'rows': pre_drop_size[0] - post_drop_size[0], 'columns': pre_drop_size[1] - post_drop_size[1]}
    data_log.intra_country_trade_dropped = data_log.intra_country_trade_dropped + ', Observations excluded by user: ' + str(dropped_dims)
    if specification.verbose is True:
        print('drop_intratrade: ' + data_log.intra_country_trade_dropped)
    return data_frame, data_log


def _drop_importers(data_frame,
                     specification,
                     meta_data,
                     data_log):
    pre_drop_size = data_frame.shape
    if (len(specification.drop_imp_exp) > 0) or (len(specification.drop_imp) > 0):
        importer_drop_list = list(set(specification.drop_imp_exp + specification.drop_imp))
        data_frame.drop(data_frame.loc[data_frame[meta_data.imp_var_name].isin(importer_drop_list)].index, inplace=True)
        data_log.importers_dropped = str(importer_drop_list)
    else:
        data_log.importers_dropped = 'none'
    post_drop_size = data_frame.shape
    dropped_dims = {'rows': pre_drop_size[0] - post_drop_size[0], 'columns': pre_drop_size[1] - post_drop_size[1]}
    data_log.importers_dropped = data_log.importers_dropped + ', Observations excluded by user: ' + str(dropped_dims)
    if specification.verbose is True:
        print('drop_imp: ' + data_log.importers_dropped)
    return data_frame, data_log


def _drop_exporters(data_frame,
                     specification,
                     meta_data,
                     data_log):
    pre_drop_size = data_frame.shape
    if (len(specification.drop_imp_exp) > 0) or (len(specification.drop_exp) > 0):
        exporter_drop_list = list(set(specification.drop_imp_exp + specification.drop_exp))
        data_frame.drop(data_frame.loc[data_frame[meta_data.exp_var_name].isin(exporter_drop_list)].index, inplace=True)
        data_log.exporters_dropped = str(exporter_drop_list)
    else:
        data_log.exporters_dropped = 'none'
    post_drop_size = data_frame.shape
    dropped_dims = {'rows': pre_drop_size[0] - post_drop_size[0], 'columns': pre_drop_size[1] - post_drop_size[1]}
    data_log.exporters_dropped = data_log.exporters_dropped + ', Observations excluded by user: ' + str(dropped_dims)
    if specification.verbose is True:
        print('drop_exp: ' + data_log.exporters_dropped)
    return data_frame, data_log

def _keep_importers(data_frame,
                     specification,
                     meta_data,
                     data_log):
    pre_drop_size = data_frame.shape
    if (len(specification.keep_imp_exp) > 0) or (len(specification.keep_imp) > 0):
        importer_keep_list = list(set(specification.keep_imp_exp + specification.keep_imp))
        data_frame = data_frame.loc[data_frame[meta_data.imp_var_name].isin(importer_keep_list)]
        data_log.importers_kept = str(importer_keep_list)
    else:
        data_log.importers_kept = 'all available'
    post_drop_size = data_frame.shape
    dropped_dims = {'rows': pre_drop_size[0] - post_drop_size[0], 'columns': pre_drop_size[1] - post_drop_size[1]}
    data_log.importers_kept = data_log.importers_kept + ', Observations excluded by user: ' + str(dropped_dims)
    if specification.verbose is True:
        print('keep_imp: ' + data_log.importers_kept)
    return data_frame, data_log

def _keep_exporters(data_frame,
                     specification,
                     meta_data,
                     data_log):
    pre_drop_size = data_frame.shape
    if (len(specification.keep_imp_exp) > 0) or (len(specification.keep_exp) > 0):
        exporter_keep_list = list(set(specification.keep_imp_exp + specification.keep_exp))
        data_frame = data_frame.loc[data_frame[meta_data.exp_var_name].isin(exporter_keep_list)]
        data_log.exporters_kept = str(exporter_keep_list)
    else:
        data_log.exporters_kept = 'all available'
    post_drop_size = data_frame.shape
    dropped_dims = {'rows': pre_drop_size[0] - post_drop_size[0], 'columns': pre_drop_size[1] - post_drop_size[1]}
    data_log.exporters_kept = data_log.exporters_kept + ', Observations excluded by user: ' + str(dropped_dims)
    if specification.verbose is True:
        print('keep_exp: ' + data_log.exporters_kept)
    return data_frame, data_log

def _drop_years(data_frame,
                     specification,
                     meta_data,
                     data_log):
    pre_drop_size = data_frame.shape
    if len(specification.drop_years) > 0:
        data_frame = data_frame.loc[data_frame[meta_data.year_var_name].isin(specification.drop_years)]
        data_log.years_dropped = str(specification.dropped_years)
    else:
        data_log.years_dropped = 'none'
    post_drop_size = data_frame.shape
    dropped_dims = {'rows': pre_drop_size[0] - post_drop_size[0], 'columns': pre_drop_size[1] - post_drop_size[1]}
    data_log.years_dropped = data_log.years_dropped + ', Observations excluded by user: ' + str(dropped_dims)
    if specification.verbose is True:
        print('drop_years: ' + data_log.years_dropped)
    return data_frame, data_log

def _keep_years(data_frame,
                     specification,
                     meta_data,
                     data_log):
    pre_drop_size = data_frame.shape
    if len(specification.keep_years) > 0:
        data_frame = data_frame.loc[data_frame[meta_data.year_var_name].isin(specification.keep_years)]
        data_log.years_kept = str(specification.keep_years)
    else:
        data_log.years_kept = 'all available'
    post_drop_size = data_frame.shape
    dropped_dims = {'rows': pre_drop_size[0] - post_drop_size[0], 'columns': pre_drop_size[1] - post_drop_size[1]}
    data_log.years_kept = data_log.years_kept + ', Observations excluded by user: ' + str(dropped_dims)
    if specification.verbose is True:
        print('keep_years: ' + data_log.years_kept)
    return data_frame, data_log

def _drop_missing(data_frame,
                     specification,
                     data_log):
    pre_drop_size = data_frame.shape
    if specification.drop_missing is True:
        data_frame = data_frame.loc[data_frame.notnull().all(axis = 1)]
        data_log.missing_dropped = 'yes'
    else:
        data_log.missing_dropped = 'no'
    post_drop_size = data_frame.shape
    dropped_dims = {'rows': pre_drop_size[0] - post_drop_size[0], 'columns': pre_drop_size[1] - post_drop_size[1]}
    data_log.missing_dropped = data_log.missing_dropped + ', Observations excluded by user: ' + str(dropped_dims)
    if specification.verbose is True:
        print('drop_missing: ' + data_log.missing_dropped)
    return data_frame, data_log
