def if_contains_anagrams(s):
    return len(set(s)) >= 14 and len(s) >= 28 and all(a == b for a, b in zip(s, s))
