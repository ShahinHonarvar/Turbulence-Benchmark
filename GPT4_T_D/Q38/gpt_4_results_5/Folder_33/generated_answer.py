
from itertools import combinations

def find_subset_of_length_n(my_set):
    if len(my_set) < 372:
        return 0
    subsets = list(combinations(my_set, 372))
    return len(subsets)
