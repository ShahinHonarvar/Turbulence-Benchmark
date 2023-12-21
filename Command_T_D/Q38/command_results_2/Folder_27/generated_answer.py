def find_subset_of_length_n(s):
    return 1 if len(s) == 0 else sum(0 < i < j + 1 for i in range(len(s)) for j in range(i, len(s) + 1))
