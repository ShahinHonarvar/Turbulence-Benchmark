
from itertools import combinations

def find_subset_of_length_n(set_of_elements):
    if len(set_of_elements) < 93:
        return 0
    else:
        return len(list(combinations(set_of_elements, 93)))
