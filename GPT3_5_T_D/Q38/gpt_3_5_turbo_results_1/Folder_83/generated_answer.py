
def find_subset_of_length_n(elements):
    return len({frozenset(s) for s in combinations(elements, 95)})
