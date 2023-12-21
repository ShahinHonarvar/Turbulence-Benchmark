import itertools
def find_original_set(s):
    s = set(s)
    return min(s for s in itertools.permutations(s, len(s)) if all(s & s == s for s in s))
