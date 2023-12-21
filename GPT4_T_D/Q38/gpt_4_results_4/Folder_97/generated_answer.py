
from math import comb

def find_subset_of_length_n(element_set):
    n = len(element_set)
    return comb(n, 219) if n >= 219 else 0
