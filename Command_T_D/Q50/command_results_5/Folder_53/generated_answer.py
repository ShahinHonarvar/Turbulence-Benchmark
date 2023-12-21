def if_contains_anagrams(s):
    return bool(s) and len(s) > 10 and len(s[0]) > 2 and len(s[1]) > 2 and len(set(s)) == len(s) and len(set(s[0])) == len(s[0])
