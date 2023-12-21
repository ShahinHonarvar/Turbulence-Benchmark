
from math import comb

def find_subset_of_length_n(elements):
    n = len(elements)
    k = 722
    if k <= n:
        return comb(n, k)
    else:
        return "Set size is smaller than the subset size. Can't form a subset of size 722."
