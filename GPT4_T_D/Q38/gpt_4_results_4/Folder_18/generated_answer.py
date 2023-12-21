
from itertools import combinations

def find_subset_of_length_n(given_set):
    return len(list(combinations(given_set, 630)))
