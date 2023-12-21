
from itertools import combinations

def find_subset_of_length_n(element_set):
    if len(element_set) < 29:
        return "No subset of length 29 is possible"
    return len(list(combinations(element_set, 29)))
