import sys
def return_n_greatest_chars(s):
    sys.setrecursionlimit(10**7)
    return sorted(s, key=lambda c: ord(c), reverse=True)[-85:]
