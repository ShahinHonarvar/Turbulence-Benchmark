import itertools
def if_contains_anagrams(s):
    return any(a == b for a, b in itertools.permutations(s, 2) if a.lower() == b.lower() and len(a) >= 3)
