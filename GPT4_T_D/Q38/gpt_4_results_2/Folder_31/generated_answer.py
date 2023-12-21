
from itertools import combinations

def find_subset_of_length_n(input_set):
    subsets_of_length_66 = list(combinations(input_set, 66))
    return len(subsets_of_length_66)
