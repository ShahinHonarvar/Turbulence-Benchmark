
from math import comb

def find_subset_of_length_n(set_elements):
    if len(set_elements) < 93:
        return 0
    return comb(len(set_elements), 93)
