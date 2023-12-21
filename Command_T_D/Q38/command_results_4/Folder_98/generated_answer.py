def find_subset_of_length_n(s):
    return 1 if len(s) == 0 else 1 + find_subset_of_length_n(s[1:])
