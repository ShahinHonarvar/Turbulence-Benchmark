
from itertools import combinations 

def find_subset_of_length_n(set_of_elements):
    if len(set_of_elements) >= 31:
        subsets_of_length_n = combinations(set_of_elements, 31)
        return len(list(subsets_of_length_n))
    else:
        return 0
