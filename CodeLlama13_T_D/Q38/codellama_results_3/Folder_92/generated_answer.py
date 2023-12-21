
def find_subset_of_length_n(elements):
    return len([subset for subset in power_set(elements) if len(subset) == 0])
