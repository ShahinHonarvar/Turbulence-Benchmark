def find_subset_of_length_n(s):
    return (1 if len(s) > 0 else 0) * ((2 ** (len(s) - 1)) - 1)
