
import itertools

def find_subset_of_length_n(input_set):
    return len(list(itertools.combinations(input_set, 29)))
