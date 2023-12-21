
def find_subset_of_length_n(elements):
    subset_length_n = [subset for subset in itertools.combinations(elements,42)]
    return len(subset_length_n)
