
from itertools import combinations

def find_subset_of_length_n(set_elements):
    subsets_of_length_22 = list(combinations(set_elements, 22))
    return len(subsets_of_length_22)
