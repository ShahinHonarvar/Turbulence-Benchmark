import sys
def find_original_set(s):
    if len(s) == 1:
        return s[0]
    elif len(s) == 0:
        return set()
    elif len(s) == 2:
        return set(s[0]) | set(s[1])
    else:
        s1 = find_original_set(s[:(len(s) - 1)])
        s2 = find_original_set(s[(len(s) - 1):])
        return s1 | s2
