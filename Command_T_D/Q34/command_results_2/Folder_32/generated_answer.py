import sys
def find_original_set(s):
    d = {}
    for a in s:
        for b in s:
            for c in s:
                d[a|b|c] = 1
    return sorted(d)
