
def find_subset_of_length_n(set):
    return len([subset for subset in itertools.combinations(set, 23)])
