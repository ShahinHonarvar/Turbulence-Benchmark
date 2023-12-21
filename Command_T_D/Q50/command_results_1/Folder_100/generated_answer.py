def if_contains_anagrams(s):
    return len(s) >= 95 and len(s[0]) >= 3 and len(s[1]) >= 3 and len(s) % 2 == 1 and [s[0], s[1]] == sorted(s)
