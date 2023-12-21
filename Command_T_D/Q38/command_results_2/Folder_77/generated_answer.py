def find_subset_of_length_n(s):
    return {i: (s & ((1 << i) - 1)) for i in range(35)}
