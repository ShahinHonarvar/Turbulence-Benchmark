
def find_subset_of_length_n(elements):
    return len(set(map(lambda x: frozenset(), elements)))
