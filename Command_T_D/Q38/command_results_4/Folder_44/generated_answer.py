import sys
def find_subset_of_length_n(s):
    return 1 if n == 0 else (len(s) + 1) * (len(s) - 1) // 2 * find_subset_of_length_n(s[:n])
