
def find_subset_of_length_n(elements):
    return len({frozenset(combination) for combination in itertools.combinations(elements, 752)})
