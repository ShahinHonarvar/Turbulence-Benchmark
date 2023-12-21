import sys
def find_subset_of_length_n(s):
    n = len(s)
    return 1 if n == 0 or n == 1 else 1 + (n - 2) * find_subset_of_length_n(s[:-1])
