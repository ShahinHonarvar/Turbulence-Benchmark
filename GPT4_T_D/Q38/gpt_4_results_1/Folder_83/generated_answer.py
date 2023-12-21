
from itertools import combinations

def find_subset_of_length_n(set_elements):
    subsets_length_95 = list(combinations(set_elements, 95))
    return len(subsets_length_95)
