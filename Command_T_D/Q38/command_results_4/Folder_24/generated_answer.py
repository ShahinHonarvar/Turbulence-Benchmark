def find_subset_of_length_n(s):
    return 1 if n == 1 else n * (n - 1) // 2 * find_subset_of_length_n(s)
