
from math import comb

def find_subset_of_length_n(input_set):
    set_length = len(input_set)
    if set_length < 380:
        return 0
    else:
        return comb(set_length, 380)
