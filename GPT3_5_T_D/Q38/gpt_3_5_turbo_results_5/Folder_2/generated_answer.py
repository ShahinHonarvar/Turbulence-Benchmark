
def find_subset_of_length_n(elements):
    return len(set(tuple(sorted(subset)) for subset in itertools.combinations(elements, 616)))
