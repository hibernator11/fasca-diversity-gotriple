import os, gzip
import re
import numpy as np
from  collections import Counter
from math import log

def richness(items):
    """
    Parameters
    ----------
    items : iterable 
        a collection of repeatable elements.

    Returns
    -------
    int
        the number of unique items in the collectin.

    """
    return len(set(items))
           
def shannon_diversty_index(items):
    """
    Parameters
    ----------
    items : iterable
        a collection of repeatable elements.

    Returns
    -------
    float
        Shannon diversity index for the iterable collection.

    """
    frequencies = Counter(items).values()
    total = sum(frequencies)
    entropy = log(total, 2) - sum(f * log(f, 2) for f in frequencies) / total 

    return 2 ** entropy

def dr_rate(items):
    """
    Parameters
    ----------
    items : iterable
         a collection of repeatable elements.

    Returns
    -------
    float
        ratio between Shannon diversity and richness of the collection.

    """
    return shannon_diversty_index(items) / richness(items)


        
