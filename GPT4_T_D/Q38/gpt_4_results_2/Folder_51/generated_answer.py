
from math import comb

def find_subset_of_length_n(s):
    if len(s) < 64:
        return 0
    return comb(len(s), 64)
