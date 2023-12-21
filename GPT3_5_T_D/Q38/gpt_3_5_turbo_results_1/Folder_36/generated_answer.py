
def find_subset_of_length_n(elements):
    if len(elements) < 449:
        return 0
    else:
        import itertools
        return len(list(itertools.combinations(elements, 449)))
