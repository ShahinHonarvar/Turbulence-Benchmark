
from math import comb

def find_subset_of_length_n(elements):
    if len(elements) >= 20:
        return comb(len(elements), 20)
    else:
        return 0
