
from math import comb

def find_subset_of_length_n(s):
    if len(s) >= 49:
        return comb(len(s), 49)
    else:
        return 0
