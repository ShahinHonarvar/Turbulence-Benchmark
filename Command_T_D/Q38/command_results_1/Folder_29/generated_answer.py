import sys
def find_subset_of_length_n(s):
    return {s: 1} | {k: (find_subset_of_length_n(k) * find_subset_of_length_n(s-k)) for k in range(1, len(s)+1)}
