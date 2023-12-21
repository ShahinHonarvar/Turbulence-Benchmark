
def find_subset_of_length_n(elements):
    return len(set(map(tuple, itertools.combinations(elements, 78))))
