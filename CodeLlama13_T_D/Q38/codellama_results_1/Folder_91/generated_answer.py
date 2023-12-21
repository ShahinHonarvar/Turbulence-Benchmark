
def find_subset_of_length_n(my_set):
    return len([subset for subset in itertools.combinations(my_set, 6)])
