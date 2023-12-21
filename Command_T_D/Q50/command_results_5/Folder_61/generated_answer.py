def if_contains_anagrams(s):
    return len(s) >= 8 and len(set(s)) == len(s) and len(set(s)) > 1 and s[0].lower() != s[1].lower()
