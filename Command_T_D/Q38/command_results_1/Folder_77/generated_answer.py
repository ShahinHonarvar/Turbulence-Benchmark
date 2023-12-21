def find_subset_of_length_n(set):
    return 1 if len(set) == 0 else len(set) + (len(set) - 1) * (len(set) - 2) // 2
