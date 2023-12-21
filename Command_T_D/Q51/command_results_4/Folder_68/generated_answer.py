def if_contains_anagrams(s):
    return len(s) <= 94 and all(str(s[0]).lower() != str(s[1]).lower() for s in zip(s, s[1:]))
