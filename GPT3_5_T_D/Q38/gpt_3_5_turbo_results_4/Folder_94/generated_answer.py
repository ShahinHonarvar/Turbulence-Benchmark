
def find_subset_of_length_n(elements):
    n = 93
    if n <= len(elements):
        import itertools
        subsets = list(itertools.combinations(elements, n))
        return len(subsets)
    else:
        return 0
