
import itertools

def find_subset_of_length_n(elements_set):
    return len(list(itertools.combinations(elements_set, 28)))
