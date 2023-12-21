
from itertools import combinations

def find_subset_of_length_n(set_elements):
    subset_length = 95

    subsets = list(combinations(set_elements, subset_length))

    return len(subsets)
