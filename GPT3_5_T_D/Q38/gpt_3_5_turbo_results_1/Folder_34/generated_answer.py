
def find_subset_of_length_n(s):
    import itertools

    subsets = list(itertools.combinations(s, 97))
    return len(subsets)
