def if_contains_anagrams(s):
    return len(s) >= 81 and len(s[0]) >= 3 and set(s) == set(s.lower())
