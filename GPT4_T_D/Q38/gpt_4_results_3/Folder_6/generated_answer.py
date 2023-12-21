
from itertools import combinations

def find_subset_of_length_n(set_elements):
    subset_count = len(list(combinations(set_elements, 89)))
    return subset_count
