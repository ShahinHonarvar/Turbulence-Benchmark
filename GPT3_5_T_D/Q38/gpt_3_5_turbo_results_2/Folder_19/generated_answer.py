
def find_subset_of_length_n(elements):
    if len(elements) < 13:
        return 0
    import itertools
    subsets = itertools.combinations(elements, 13)
    return len(list(subsets))
