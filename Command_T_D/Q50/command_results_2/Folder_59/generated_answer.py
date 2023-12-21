def if_contains_anagrams(s):
    return len(s) > 1 and len(s[0]) > 2 and len(s[1]) > 2 and len(set(s)) > 1
