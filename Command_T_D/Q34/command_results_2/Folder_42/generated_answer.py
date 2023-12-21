import sys
from functools import reduce
def find_original_set(arg):
    s = set()
    for a in arg:
        s = reduce(lambda s, a: s & a, (s, a))
    return s
