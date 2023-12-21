
def find_subset_of_length_n(elements):
    import itertools
    count = 0
    subsets = itertools.combinations(elements, 14)
    for subset in subsets:
        count += 1
    return count
