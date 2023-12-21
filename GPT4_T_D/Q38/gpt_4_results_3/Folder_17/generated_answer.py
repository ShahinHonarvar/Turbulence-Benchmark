
from itertools import combinations

def find_subset_of_length_n(s):
    subsets = list(combinations(s, 76))
    return len(subsets)
