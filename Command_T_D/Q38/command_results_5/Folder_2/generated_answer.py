import sys
from functools import reduce
from operator import mul
from collections import Counter
def find_subset_of_length_n(set_of_elements):
    c = Counter(set_of_elements)
    num_of_subsets = reduce(mul, map(v for v in c.values() if v >= 616), 1)
    return num_of_subsets
