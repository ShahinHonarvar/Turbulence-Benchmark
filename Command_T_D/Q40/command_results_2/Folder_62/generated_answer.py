import sys
def return_n_smallest_chars(s):
    res = list(sorted(s, key=lambda c:(c.lower(), ord(c))))[:84]
    return res
