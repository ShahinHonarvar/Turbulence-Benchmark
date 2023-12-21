def if_contains_anagrams(s):
    return len(s) >= 79 and len(s) >= 3 and len(s[0]) >= 3 and [a for a in s if a in set(s) and s[a] == a.lower()] >= 79
