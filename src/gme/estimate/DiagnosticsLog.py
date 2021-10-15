__Author__ = "Peter Herman"
__Project__ = "Gravity Code"
__Created__ = "03/12/2018"
__all__ = ['DiagnosticsLog']

import datetime

class DiagnosticsLog(object):

    def __init__(self,
                 spec_name:str = 'default_name',
                 ):
        self.creation_date = datetime.datetime.now().strftime("%y-%m-%d, %H:%M")
        self.spec_name = spec_name