def find_subset_of_length_n(s):
    return sum(1 for x in range(len(s) + 1) if len(s & ((1 << x) - 1)) == 46)
