import sys
def find_subset_of_length_n(s):
    return 1 + sum(1 for i in range(len(s)) if s[i] == 1)
