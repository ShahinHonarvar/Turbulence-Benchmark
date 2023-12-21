
from math import comb

def find_subset_of_length_n(set_elems):
    if len(set_elems) < 327:
        return 0
    else:
        return comb(len(set_elems), 327)
