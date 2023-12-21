
def find_subset_of_length_n(elements, n):
    return len(set(itertools.combinations(elements, n)))
