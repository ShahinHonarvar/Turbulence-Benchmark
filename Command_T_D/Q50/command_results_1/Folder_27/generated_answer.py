import itertools
def if_contains_anagrams(s):
    anagrams = set(x for x in itertools.permutations(x.lower() for x in s if len(x) >= 3))
    return len(anagrams) >= 86
