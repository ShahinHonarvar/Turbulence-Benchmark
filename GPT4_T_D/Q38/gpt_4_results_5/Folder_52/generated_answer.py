
from itertools import combinations

def find_subset_of_length_n(elements):
    count_subsets = len(list(combinations(elements, 32)))
    return count_subsets
