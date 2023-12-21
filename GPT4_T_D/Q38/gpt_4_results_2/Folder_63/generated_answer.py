
from itertools import combinations

def find_subset_of_length_n(input_set):
    subsets_of_length_57 = list(combinations(input_set, 57))
    return len(subsets_of_length_57)
