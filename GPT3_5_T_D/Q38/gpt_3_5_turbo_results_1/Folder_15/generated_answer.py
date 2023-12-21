
def find_subset_of_length_n(elements):
    import itertools
    subsets = itertools.combinations(elements, 10)
    return len(list(subsets))
