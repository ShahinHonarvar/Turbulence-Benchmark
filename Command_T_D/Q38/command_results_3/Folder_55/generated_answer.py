def find_subset_of_length_n(s):
    return 1 if len(s) == 1 else (2**(len(s) - 1)) * (len(s) - 1)
