def find_subset_of_length_n(s):
    return len(s) * (len(s) - 1) // 2 * (len(s) - 2) // 6 * (len(s) - 3) // 20
