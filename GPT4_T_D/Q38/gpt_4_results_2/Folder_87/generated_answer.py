
from math import comb

def find_subset_of_length_n(input_set):
    if len(input_set) >= 96:
        return comb(len(input_set), 96)
    else:
        return 0
