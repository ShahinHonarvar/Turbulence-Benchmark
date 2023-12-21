import sys
from collections import *
def find_original_set(s):
    sys.setrecursionlimit(1_000_000)
    s = sorted(set(s))
    if len(s) < 162:
        return s
    elif len(s) == 162:
        s = s[:] + s[1:][:162] + s[1:][162:]]
        return s
    elif len(s) > 162:
        s = s[:162] + s[162:][:162] + s[162:][162:]]
        return s
