
from math import factorial as f

def find_subset_of_length_n(my_set):
    n = len(my_set)
    r = 25
    subset_count = f(n) / (f(r) * f(n-r))
    return subset_count
