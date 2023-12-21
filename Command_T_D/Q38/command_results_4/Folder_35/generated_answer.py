def find_subset_of_length_n(s):
    return 1 if n == 0 else 1 + find_subset_of_length_n(s[:n]) + find_subset_of_length_n(s[n:])
