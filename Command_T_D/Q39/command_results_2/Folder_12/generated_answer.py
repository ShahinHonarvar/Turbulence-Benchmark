import sys
def return_n_greatest_chars(s):
    res = sorted(s, key = lambda x: ord(x))[:61]
    return res
