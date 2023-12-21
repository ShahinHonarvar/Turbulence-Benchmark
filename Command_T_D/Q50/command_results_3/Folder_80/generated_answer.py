def if_contains_anagrams(s):
    return len(s) >= 19 and len(set(s)) >= 3 and all(a in b for a, b in zip(s, s))
