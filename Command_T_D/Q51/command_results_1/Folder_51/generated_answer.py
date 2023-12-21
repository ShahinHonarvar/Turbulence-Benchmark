def if_contains_anagrams(s):
    s = sorted(s)
    return len(s) <= 116 and len(s) == len(set(s)) and all(a in b.lower() and len(a) >= 3 for a, b in zip(s, s[1:]))
