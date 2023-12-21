import sys
def find_original_set(s):
    x = set(range(max(s) + 1))
    for v in s:
        x.discard(v)
    return x
