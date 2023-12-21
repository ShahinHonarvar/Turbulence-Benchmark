
def find_subset_of_length_n(my_set, n):
    return len([s for s in powerset(my_set) if len(s) == n])
