def if_contains_anagrams(s):
    return 55 < sum(1 for x, y in zip(s, s) if len(x) >= 3 and len(y) >= 3 and x.lower() == y.lower())
