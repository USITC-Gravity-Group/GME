__author__ = "Saad Ahmad"
__project__ = "gme.estimate"
__created__ = "07-31-2018"
__edited__ = "Peter Herman"
__all__ = ['save_estimation', 'load_estimation']

import pickle
import pandas as pd
from gme.estimate.EstimationModel import EstimationModel

def save_estimation(estimation_model, filename: str):
    '''
    Save a serialized copy of an EstimationModel or other object at the specified path.
    Args:
        estimation_model: object
            The object to be saved.
        filename: str
            The path and file name under which to save the object.

    Returns: None

    Examples:
        >>> save_estimation(sample_model, "c:\\Documents\\saved_object.p")

    '''
    f = open(filename, "wb")
    pickle.dump(estimation_model, f)



def load_estimation(filename: str):
    '''
    Load a saved estimation model
    Args:
        filename: str
            The path and file name under which an object was saved.

    Returns: object
        A loaded instance of the specified object.

    Examples:
        >>> loaded_model = load_estimation("c:\\Documents\\saved_object.p")
    '''
    f = open(filename, 'rb')
    estimation_model = pickle.load(f)
    f.close
    return estimation_model
