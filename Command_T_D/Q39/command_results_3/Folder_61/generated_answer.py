import sys
def return_n_greatest_chars(str):
    return list(sorted(str, key = lambda c: sys.maxsize - ord(c)))[:66]
