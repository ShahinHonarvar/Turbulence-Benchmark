
def find_subset_of_length_n(elements):
    return len([subset for subset in powerset(elements) if len(subset) == 99])
