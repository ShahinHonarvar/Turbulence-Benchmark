def if_contains_anagrams(s):
    return len(set(s)) <= 25 and len(s) > 2 and all(set(a) == set(b) for a, b in zip(s, s))
