def if_contains_anagrams(s):
    return (len(s) >= 40 and len(s[0]) >= 3) and len(s[0]) * len(s[1]) >= 40
