import sys
def find_subset_of_length_n(s):
    return 1 if len(s) == 0 else sum(find_subset_of_length_n(s[:i]) for i in range(len(s) + 1))
