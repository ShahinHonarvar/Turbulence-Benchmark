import sys
def return_n_smallest_chars(str_):
    res = str_.split()[:83]
    res.sort()
    return res
