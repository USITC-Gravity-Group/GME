__author__ = "Peter Herman"
__project__ = "gme.estimate"
__created__ = "05-16-2018"
__all__ = ['coefficient_kd_plot']

import pandas as pd
from .EstimationModel import EstimationModel
import matplotlib.pyplot as plt
from typing import List


def coefficient_kd_plot(estimation_model: EstimationModel,
                        variables: List[str],
                        path: str = None,
                        bandwidth: float = 0.5,
                        rename_variables: dict = None):
    """
    Produce kernel density plots of parameter estimates across different sectors in the results dictionary.

    Args:
        estimation_model: gme.EstimationModel
            An estimated EstimationModel with more than one sector.
        variables: List(str)
            A list of model covariates for which to plot kernel densities.
        path: (optional) str
            A path and file name at which to save the plot.
            Can end in the following file types for example: pdf, svg, and png.
        bandwidth: float
            Specify the bandwidth for the density plots. The default is 0.5.
        rename_variables: (optional)
            A dictionary of alternative variable names to use in the plot.
            For example {'original_name':'new_name}

    Returns: None
    """
    if estimation_model.results_dict is None:
        raise ValueError("results_dict does not exist. Must estimate model first.")

    results_dict = estimation_model.results_dict
    dict_key = results_dict.keys()
    coeff_df = pd.DataFrame(columns=variables)
    for var in variables:
        coefficients = []
        for key in dict_key:
            coefficients.append(results_dict[key].params[var])
        coeff_df[var] = pd.Series(coefficients)

    if rename_variables is not None:
        coeff_df.rename(columns=rename_variables, inplace=True)
    coeff_df.plot(kind='density', bw_method=bandwidth, subplots=True)

    if path is not None:
        plt.savefig(path)
