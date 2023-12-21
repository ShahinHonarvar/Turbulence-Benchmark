
from math import comb

def find_subset_of_length_n(elements_set):
    if len(elements_set) < 84:
        return "Not enough elements in the set"
    else:
        return comb(len(elements_set), 84)
