
def find_subset_of_length_n(elements):
    import itertools
    subsets = itertools.combinations(elements, 85)
    count = 0
    for subset in subsets:
        count += 1
    return count
