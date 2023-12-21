
from math import comb

def find_subset_of_length_n(set_elements):
    if len(set_elements) < 67:
        return "Set does not have sufficient elements"
    else:
        return comb(len(set_elements), 67)
