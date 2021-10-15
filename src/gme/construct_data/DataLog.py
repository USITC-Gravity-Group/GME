__Author__ = "Peter Herman"
__Project__ = "Gravity Code"
__Created__ = "03/12/2018"
__all__ = ['DataLog']

import datetime

class DataLog(object):

    def __init__(self,
                 parent_logs = []):
        self.parent_logs = parent_logs
        self.creation_date = datetime.datetime.now().strftime("%y-%m-%d, %H:%M")

        # --------------------
        # Part of _estimate()
        # --------------------

        # Part of _slice_data_for_estimation
        self.intra_country_trade_dropped = 'not affected'
        self.importers_dropped = 'not_affected'
        self.exporters_dropped = 'not affected'
        self.importers_kept = 'not affected'
        self.exporters_kept = 'not affected'
        self.years_dropped = 'not affected'
        self.years_kept = 'not affected'
        self.missing_dropped = 'not affected'
