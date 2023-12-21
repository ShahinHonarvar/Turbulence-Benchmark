
def find_subset_of_length_n(elements):
    import itertools
    subsets = list(itertools.combinations(elements, 15))
    return len(subsets)
