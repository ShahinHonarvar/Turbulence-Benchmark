def find_subset_of_length_n(S):
    return len(set(S)) * (len(S) - 1) * (len(S) - 2) / 6
