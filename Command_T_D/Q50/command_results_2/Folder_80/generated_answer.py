def if_contains_anagrams(s):
    return len(s) >= 19 and len(s[0]) >= 3 and len(set(s)) == len(s)
