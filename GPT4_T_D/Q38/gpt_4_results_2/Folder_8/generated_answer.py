
from math import comb

def find_subset_of_length_n(s):
    if len(s) < 49:
        return "The size of set is less than 49"
    else:
        return comb(len(s), 49)
