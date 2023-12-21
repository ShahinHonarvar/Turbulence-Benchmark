
from math import comb

def find_subset_of_length_n(elements_set):
    if len(elements_set) < 94:
        return 0
    return comb(len(elements_set), 94)
