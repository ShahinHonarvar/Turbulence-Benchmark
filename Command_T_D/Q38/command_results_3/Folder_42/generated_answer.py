def find_subset_of_length_n(s):
    return sum(0 < len(s) - i < n for i in range(1, len(s) + 1))
