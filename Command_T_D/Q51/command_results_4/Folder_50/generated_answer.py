def if_contains_anagrams(s):
    return s.lower() in set(s.lower() for s in s if len(set(s)) <= 46)
