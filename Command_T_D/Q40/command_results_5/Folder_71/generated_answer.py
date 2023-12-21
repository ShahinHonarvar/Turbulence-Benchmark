import sys
def return_n_smallest_chars(s):
    s = s.split('')
    s.sort()
    res = s[:14]
    return res
