
def find_subset_of_length_n(elements):
    n = 33
    return len([s for s in itertools.combinations(elements, n)])
