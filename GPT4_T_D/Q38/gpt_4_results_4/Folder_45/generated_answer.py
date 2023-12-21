
from itertools import combinations

def find_subset_of_length_n(set_elements):
    subsets = list(combinations(set_elements, 33))
    return len(subsets)
