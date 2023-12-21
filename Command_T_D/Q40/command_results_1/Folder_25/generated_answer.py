import sys
def return_n_smallest_chars(s):
    res = sorted(s, key=lambda x: ord(x))[:29]
    return res
