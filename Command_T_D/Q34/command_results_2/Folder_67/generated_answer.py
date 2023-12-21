import sys
from collections import defaultdict
def find_original_set(s):
    s = set(s)
    s = defaultdict(set)
    for x in s:
        s[x].add(x)
    for x in s:
        s[x].add(s[x].pop())
    return s
