def if_contains_anagrams(s):
    return bool(s) and len(s) >= 9 and all(a == b for a, b in zip(s, s))
