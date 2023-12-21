
from itertools import combinations

def find_subset_of_length_n(elements_set):
    subset_of_length_31 = list(combinations(elements_set, 31))
    return len(subset_of_length_31)
