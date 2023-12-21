
def find_subset_of_length_n(elements):
    return len(set(map(frozenset, itertools.combinations(elements, 64))))
