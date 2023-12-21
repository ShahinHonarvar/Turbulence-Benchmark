
from math import comb

def find_subset_of_length_n(set_of_elements):
    if len(set_of_elements) < 29:
        return "Error: The size of the set is less than 29."
    return comb(len(set_of_elements), 29)
