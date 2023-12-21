import sys
def return_n_greatest_chars(s):
    sys.setrecursionlimit(10**6)
    return sorted(s, key=lambda x: ord(x))[:21]
