def find_subset_of_length_n(s):
    return 0 if not s else len(s) * (len(s) + 1) // 2
