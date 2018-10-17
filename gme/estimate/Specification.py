__Author__ = "Peter Herman"
__Project__ = "Gravity Code"
__Created__ = "03/12/2018"

from typing import List

class Specification(object):
    def __init__(self,
                 spec_name:str = 'default_name',
                 lhs_var: str = None,
                 rhs_var: List[str] = None,
                 sector_by_sector: bool = False,
                 drop_imp_exp: List[str] = [],
                 drop_imp: List[str] = [],
                 drop_exp: List[str] = [],
                 keep_imp_exp: List[str] = [],
                 keep_imp: List[str] = [],
                 keep_exp: List[str] = [],
                 drop_years: List[str] = [],
                 keep_years: List[str] = [],
                 drop_missing: bool = False,
                 variables_to_drop_missing: List[str] = [],
                 fixed_effects:List[str] = [],
                 omit_fixed_effect:List[str] = [],
                 std_errors:str = 'HC1',
                 iteration_limit:int = 1000,
                 drop_intratrade:bool = True,
                 verbose:bool = True):
        if lhs_var is None:
            raise ValueError('lhs_var (left hand side variable) must be specified.')

        self.spec_name = spec_name
        self.lhs_var = lhs_var
        self.rhs_var = rhs_var
        self.sector_by_sector = sector_by_sector
        self.drop_imp_exp = drop_imp_exp
        self.drop_imp = drop_imp
        self.drop_exp = drop_exp
        self.keep_imp_exp = keep_imp_exp
        self.keep_imp = keep_imp
        self.keep_exp = keep_exp
        self.drop_years = drop_years
        self.keep_years = keep_years
        self.drop_missing = drop_missing
        self.variables_to_drop_missing = variables_to_drop_missing
        self.fixed_effects = fixed_effects
        self.omit_fixed_effect = omit_fixed_effect
        self.std_errors = std_errors
        self.iteration_limit = iteration_limit
        self.drop_intratrade = drop_intratrade
        self.verbose = verbose