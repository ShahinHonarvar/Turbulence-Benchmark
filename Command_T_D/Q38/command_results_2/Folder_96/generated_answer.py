import sys
from collections import Counter
def find_subset_of_length_n(set_of_elements):
    # function to find the number of all its subsets of size 47
    # takes one argument, a set of elements
    # returns the number of all its subsets of size 47
    cnt = Counter(set_of_elements)
    return 1 if 47 in cnt else 0
