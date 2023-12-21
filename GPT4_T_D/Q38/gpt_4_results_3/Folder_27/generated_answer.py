
from math import comb

def find_subset_of_length_n(set_elements):
    set_length = len(set_elements)
    if set_length < 56:    
        return 0
    else:
        return comb(set_length, 56)
