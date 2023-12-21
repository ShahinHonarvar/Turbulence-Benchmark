import itertools
def if_contains_anagrams(s):
    return any(a.lower() == b.lower() for a, b in itertools.permutations(s, 2) if len(a) >= 3 and len(b) >= 3)
