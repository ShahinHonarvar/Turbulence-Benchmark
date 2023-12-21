import sys
def find_original_set(s):
    if not s:
        return set()
    s = sorted(s)
    a = set(s[0])
    for b in s[1:]:
        a &= b
    return a
