def if_contains_anagrams(s):
    return sum(a in b.lower() for a, b in zip(s, s)) >= 314
