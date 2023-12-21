
from itertools import combinations

def find_subset_of_length_n(elem_set):
    return len(list(combinations(elem_set, 33)))
