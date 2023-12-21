def if_contains_anagrams(s):
    return len(s) > 188 and len(s[0]) > 2 and len(s[1]) > 2 and len(s[0]) == len(s[1]) and set(s[0].lower()) == set(s[1].lower())
