
from math import comb

def find_subset_of_length_n(set_of_elements):
    set_length = len(set_of_elements)
    if set_length < 66:
        return 0
    else:
        return comb(set_length, 66)
