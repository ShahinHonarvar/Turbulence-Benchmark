
def find_subset_of_length_n(s):
    import itertools
    subsets = list(itertools.combinations(s, 74))
    return len(subsets)
