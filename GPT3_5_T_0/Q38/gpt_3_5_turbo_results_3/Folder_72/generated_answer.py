
def find_subset_of_length_n(elements):
    import itertools
    count = 0
    for subset in itertools.combinations(elements, 16):
        count += 1
    return count
