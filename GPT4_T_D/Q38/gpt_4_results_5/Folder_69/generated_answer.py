
from math import comb

def find_subset_of_length_n(set_of_elements):
    n = 894
    if len(set_of_elements) < n:
        return 0
    else:
        return comb(len(set_of_elements), n)
