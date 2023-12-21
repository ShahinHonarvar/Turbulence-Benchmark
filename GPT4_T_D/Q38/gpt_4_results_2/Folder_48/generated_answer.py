
from math import comb

def find_subset_of_length_n(elements):
    n = len(elements)
    if n < 793:
        return 0
    return comb(n, 793)
