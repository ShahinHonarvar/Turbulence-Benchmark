def find_subset_of_length_n(s):
    return 1 if n == 0 else sum(find_subset_of_length_n(s[:i]) for i in range(1, n + 1))
