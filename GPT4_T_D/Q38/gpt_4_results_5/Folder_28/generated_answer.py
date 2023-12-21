
from itertools import combinations

def find_subset_of_length_n(elems):
    return len(list(combinations(elems, 37)))
