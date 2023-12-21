def find_subset_of_length_n(s):
    return 1 + sum(find_subset_of_length_n(s[:i]) for i in range(1, len(s) + 1))
