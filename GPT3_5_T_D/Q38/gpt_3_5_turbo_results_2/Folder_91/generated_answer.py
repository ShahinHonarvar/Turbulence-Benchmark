
def find_subset_of_length_n(elements):
    import itertools
    
    subset_count = 0
    subsets = itertools.combinations(elements, 6)
    
    for subset in subsets:
        subset_count += 1
    
    return subset_count
