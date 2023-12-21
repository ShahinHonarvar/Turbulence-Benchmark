
from itertools import combinations

def find_subset_of_length_n(input_set):
    if len(input_set) < 41: return 0 
    return len(list(combinations(input_set, 41)))
