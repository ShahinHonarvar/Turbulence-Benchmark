
def find_subset_of_length_n(elements):
    return len(set([frozenset(x) for x in combinations(elements, 66)]))
