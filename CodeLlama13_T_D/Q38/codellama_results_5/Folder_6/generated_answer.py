
def find_subset_of_length_n(set, n):
    return len([s for s in powerset(set) if len(s) == n])
