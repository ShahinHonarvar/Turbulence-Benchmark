def find_subset_of_length_n(s):
    return sum(1 for i in range(len(s) - 98) for j in range(i + 1, len(s) - 1))
