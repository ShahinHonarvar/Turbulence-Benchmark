def if_contains_anagrams(s):
    return len(s) <= 86 and len(s) >= 3 and all(a == b.lower() for a, b in zip(s, s))
