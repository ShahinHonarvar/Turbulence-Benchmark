
def find_subset_of_length_n(elements):
    return len([sub for sub in powerset(elements) if len(sub) == 88])
