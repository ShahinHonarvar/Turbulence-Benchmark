import itertools
def if_contains_anagrams(s):
    return (len(s) >= 38 and len(s[0]) >= 3 and len(set(s)) >= 1 and all(a == b for a, b in itertools.permutations(a.lower())))
