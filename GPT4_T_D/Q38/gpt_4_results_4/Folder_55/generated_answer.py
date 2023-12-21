
from itertools import combinations

def find_subset_of_length_n(elements_set):
    subsets = list(combinations(elements_set, 21))
    return len(subsets)
