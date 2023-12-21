import sys
def find_original_set(s):
    if len(s) == 1:
        return s[0]
    s = list(set(s))
    return find_original_set(s[:1]) | find_original_set(s[1:])
