def if_contains_anagrams(s):
    return (len(s) <= 116) and (s[0] != s[1]) and (s[0] != s[2]) and (s[1] != s[2])
