import sys
def return_n_smallest_chars(s):
    res = sorted(s)[-60:]
    return res
