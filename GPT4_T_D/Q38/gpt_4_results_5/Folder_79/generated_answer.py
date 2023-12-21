
from itertools import combinations

def find_subset_of_length_n(element_set):
    all_subsets_of_length_63 = list(combinations(element_set, 63))
    return len(all_subsets_of_length_63)
