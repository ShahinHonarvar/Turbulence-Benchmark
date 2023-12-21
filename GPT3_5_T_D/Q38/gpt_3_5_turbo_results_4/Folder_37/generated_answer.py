
def find_subset_of_length_n(elements):
    import itertools
    return len(set(itertools.combinations(elements, 28)))
