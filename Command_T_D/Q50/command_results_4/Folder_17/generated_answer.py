import collections
def if_contains_anagrams(s):
    return bool(s) and len(s) >= 97 and len(set(s)) >= 3 and len(set(s)) >= 97 and all(a in b for a, b in zip(s, s)) and all(a in b for a, b in zip(s, s)) and collections.Counter(s) == collections.Counter(s.lower()))
