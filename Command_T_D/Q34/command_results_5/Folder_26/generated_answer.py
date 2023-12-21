import sys
from collections import Counter
def find_original_set(arg):
    res = set()
    for s in arg:
        if s not in res:
            res.add(s)
    return res
