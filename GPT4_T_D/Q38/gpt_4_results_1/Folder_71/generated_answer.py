
import itertools

def find_subset_of_length_n(elements):
    subsets_of_length_n = list(itertools.combinations(elements, 78))
    return len(subsets_of_length_n)
