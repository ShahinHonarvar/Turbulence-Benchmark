def find_subset_of_length_n(s):
    return 1 + sum(len(s) - i for i in range(len(s) + 1))
