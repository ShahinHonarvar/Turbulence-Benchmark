import sys
def find_subset_of_length_n(s):
    return len(s) * (len(s) - 1) * (len(s) - 2) * (len(s) - 3) * (len(s) - 4) * (len(s) - 5) * (len(s) - 6)
