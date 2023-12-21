
def find_subset_of_length_n(set):
    return len([s for s in powerset(set) if len(s) == 57])
