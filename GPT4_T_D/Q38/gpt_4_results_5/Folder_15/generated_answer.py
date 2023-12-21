
from itertools import combinations

def find_subset_of_length_n(element_set):
    return len(list(combinations(element_set, 10)))
