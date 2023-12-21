import sys
def find_subset_of_length_n(s):
    return 1 if len(s) == 0 else sum(1 for i in range(len(s) + 1) if s.count(s[:i]) == i)
