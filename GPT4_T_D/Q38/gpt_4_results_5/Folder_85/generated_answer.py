
import itertools

def find_subset_of_length_n(s):
    return len(list(itertools.combinations(s, 23)))
