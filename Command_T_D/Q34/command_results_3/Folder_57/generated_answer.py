import sys
def find_original_set(s):
    d = {}
    for k in s:
        for j in k:
            d[j] = 1
    return sorted(set(d))
