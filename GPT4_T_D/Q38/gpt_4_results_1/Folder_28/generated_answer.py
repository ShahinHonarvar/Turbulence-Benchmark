
from itertools import combinations

def find_subset_of_length_n(elements):
    if len(elements) < 37:
        return 0
    else:
        return len(list(combinations(elements, 37)))
