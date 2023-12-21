
from math import comb

def find_subset_of_length_n(elements):
    if len(elements) < 83:
        return 0
    else:
        return comb(len(elements), 83)
