def if_contains_anagrams(s):
    return s.lower() in set(sum(a.lower() in b.lower() for a, b in zip(s, s)))
