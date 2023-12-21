import sys
def find_subset_of_length_n(s):
    return sys.setrecursionlimit(10**6) // 2 * len(s) * (len(s) - 1) // 2
