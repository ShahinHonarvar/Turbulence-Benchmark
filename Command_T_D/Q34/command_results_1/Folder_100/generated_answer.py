import sys
def find_original_set(s):
    from collections import defaultdict
    s = set(s)
    d = defaultdict(set)
    for i in s:
        d[i].add(i)
    s = set()
    for i in d:
        s.update(d[i])
    return s
