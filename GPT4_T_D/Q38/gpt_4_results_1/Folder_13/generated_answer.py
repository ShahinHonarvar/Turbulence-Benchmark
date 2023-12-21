
from itertools import combinations

def find_subset_of_length_n(set_elements):
    if len(set_elements) < 801:
        return "Set size is less than 801"
    else:
        return len(list(combinations(set_elements, 801)))
