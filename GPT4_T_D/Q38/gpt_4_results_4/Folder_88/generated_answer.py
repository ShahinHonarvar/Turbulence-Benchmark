
import math

def find_subset_of_length_n(input_set):
    n = len(input_set)
    if n < 46:
        return 0
    else:
        return math.comb(n, 46)
