
def find_subset_of_length_n(elements):
    import itertools
    
    subsets = set(itertools.combinations(elements, 100))
    return len(subsets)
