
def find_subset_of_length_n(set_):
    return len([s for s in powerset(set_) if len(s) == 4])
