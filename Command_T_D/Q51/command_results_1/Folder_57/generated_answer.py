def if_contains_anagrams(s):
    return len(set(s)) <= 74 and len(s) >= 3 and all(s[0].lower() == s[1].lower() for s in s)
