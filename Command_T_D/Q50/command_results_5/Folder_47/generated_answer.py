def if_contains_anagrams(s):
    if len(s) < 47:
        return False
    s = set(s)
    return any(a.lower() == b.lower() for a, b in zip(s, s))
