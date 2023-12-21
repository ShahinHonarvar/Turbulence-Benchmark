
from math import comb

def find_subset_of_length_n(element_set):
    if (type(element_set) != set) or (len(element_set) < 80):
        return 0
    subset_count = comb(len(element_set), 80)
    return subset_count
