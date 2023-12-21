def if_contains_anagrams(s):
    return s.lower() in ((a, b) for a, b in zip(s, s) if a == b[1:])
