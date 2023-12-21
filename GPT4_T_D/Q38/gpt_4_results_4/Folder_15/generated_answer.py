
from itertools import combinations

def find_subset_of_length_n(set_param):
    return len(list(combinations(set_param, 10)))
