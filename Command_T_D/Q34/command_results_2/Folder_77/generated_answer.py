import sys
def find_original_set(s):
    s = set(s)
    for x in range(min(s),max(s)+1):
        if s.issubset(set(range(x))):
            return set(range(x))
    return set(s)
