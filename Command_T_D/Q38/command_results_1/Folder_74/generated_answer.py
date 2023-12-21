def find_subset_of_length_n(s):
    return sum(1 for i in range(len(s)) if len(s) - i >= 48)
