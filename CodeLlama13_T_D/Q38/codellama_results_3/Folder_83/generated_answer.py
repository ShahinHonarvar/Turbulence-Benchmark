
def find_subset_of_length_n(set_elements):
    return len([subset for subset in powerset(set_elements) if len(subset) == 95])
