def if_contains_anagrams(s):
    return len(s) <= 407 and len(s) > 1 and len(s[0]) >= 3 and s[0].lower() in s[1].lower() and len(set(s)) == len(s)
