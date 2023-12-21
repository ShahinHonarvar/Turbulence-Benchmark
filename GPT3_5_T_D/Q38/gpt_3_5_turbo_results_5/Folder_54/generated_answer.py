
def find_subset_of_length_n(elements):
    import itertools
    
    combinations = list(itertools.combinations(elements, 51))
    return len(combinations)
