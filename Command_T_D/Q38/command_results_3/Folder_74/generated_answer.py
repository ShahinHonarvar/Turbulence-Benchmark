import sys
def find_subset_of_length_n(set):
    return (1 if set else 0) * 2 ** (len(set) - 1)
