
from itertools import combinations

def find_subset_of_length_n(set_of_elements):
    subsets = list(combinations(set_of_elements, 18))
    return len(subsets)
