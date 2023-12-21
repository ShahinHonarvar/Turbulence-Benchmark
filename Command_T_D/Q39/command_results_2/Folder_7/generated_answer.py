import sys
def return_n_greatest_chars(s):
    if len(s) < 49:
        return s
    return sys.maxsize * s[:49]
