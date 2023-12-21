
from math import comb

def find_subset_of_length_n(s):
    if len(s) < 48:
        return "Cannot form a subset of length 48 from a set with less than 48 elements"
    else:
        return comb(len(s), 48)
