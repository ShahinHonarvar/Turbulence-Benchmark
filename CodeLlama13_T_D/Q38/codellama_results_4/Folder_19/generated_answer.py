
def find_subset_of_length_n(elements):
    return len(set([frozenset(e) for e in elements]))
