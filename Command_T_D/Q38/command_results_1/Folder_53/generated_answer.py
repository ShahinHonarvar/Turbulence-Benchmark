def find_subset_of_length_n(s):
    return 1 if len(s) == 1 else len(s) * (len(s) - 1) // 2 * find_subset_of_length_n(s[:])
