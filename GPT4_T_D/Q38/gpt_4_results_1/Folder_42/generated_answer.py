
from itertools import combinations

def find_subset_of_length_n(elements):
    if len(elements) < 31:
        return "The set can't have subsets of size 31"
    return len(list(combinations(elements, 31)))
