import sys
def find_original_set(S):
    d = {}
    for s in S:
        s.add(s)
        for i in s:
            d[i] = s
    return d.popitem(1)[0]
