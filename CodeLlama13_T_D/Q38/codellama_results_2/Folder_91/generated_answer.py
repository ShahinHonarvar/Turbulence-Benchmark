
def find_subset_of_length_n(set, n):
    return len([x for x in powerset(set) if len(x) == n])
