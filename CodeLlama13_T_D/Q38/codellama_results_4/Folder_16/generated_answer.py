
def find_subset_of_length_n(my_set, n):
    return len([subset for subset in powerset(my_set) if len(subset) == n])
