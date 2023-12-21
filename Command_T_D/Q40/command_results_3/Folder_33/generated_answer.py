import sys
def return_n_smallest_chars(s):
    return sorted(set(s), key=str.lower)[:36]
