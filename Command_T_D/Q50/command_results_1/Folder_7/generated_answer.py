def if_contains_anagrams(s):
    return len(s) >= 178 and len(s) > 1 and len(s[0]) >= 3 and len(set(s)) >= 178 and len(set(s)) == len(s)
