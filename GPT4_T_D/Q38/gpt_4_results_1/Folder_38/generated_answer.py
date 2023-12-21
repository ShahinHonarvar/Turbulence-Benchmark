
import math

def find_subset_of_length_n(set_of_elements):
    n = len(set_of_elements)
    if n < 38:
        return 0
    else:
        return math.comb(n, 38)
