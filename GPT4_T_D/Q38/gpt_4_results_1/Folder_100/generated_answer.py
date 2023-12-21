
from math import comb

def find_subset_of_length_n(s):
    if len(s) < 99:
        return 0
    else:
        return comb(len(s), 99)
