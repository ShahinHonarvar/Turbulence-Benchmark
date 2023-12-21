
from itertools import combinations

def find_subset_of_length_n(data_set):
    return len(list(combinations(data_set, 3)))
