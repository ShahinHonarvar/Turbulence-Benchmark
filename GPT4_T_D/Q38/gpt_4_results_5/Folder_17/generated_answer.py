
from itertools import combinations

def find_subset_of_length_n(input_set):
    subsets_of_size_76 = list(combinations(input_set, 76))
    return len(subsets_of_size_76)
