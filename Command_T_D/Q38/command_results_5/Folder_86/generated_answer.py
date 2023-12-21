import sys
def find_subset_of_length_n(s):
    return 1 if len(s) == 0 else find_subset_of_length_n(s[:]) + find_subset_of_length_n(s[1:])
