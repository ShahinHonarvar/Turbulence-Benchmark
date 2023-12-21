
def find_subset_of_length_n(elements):
    return len([subset for subset in powset(elements) if len(subset) == 2])
