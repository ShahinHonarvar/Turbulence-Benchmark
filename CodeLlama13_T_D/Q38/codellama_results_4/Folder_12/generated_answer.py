
def find_subset_of_length_n(elements):
    return len([s for s in powerset(elements) if len(s) == 27])
