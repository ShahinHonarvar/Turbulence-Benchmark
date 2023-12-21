import sys
def find_subset_of_length_n(S):
    return (1 << (len(S) - 1)) - 1
