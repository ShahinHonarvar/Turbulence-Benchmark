
from itertools import combinations

def find_subset_of_length_n(input_set):
    return len(list(combinations(input_set, 25)))
