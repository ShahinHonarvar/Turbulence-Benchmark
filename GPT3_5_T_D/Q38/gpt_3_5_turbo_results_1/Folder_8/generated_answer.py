
def find_subset_of_length_n(elements):
    import itertools
    subset_count = 0
    for subset in itertools.combinations(elements, 49):
        subset_count += 1
    return subset_count
