def if_contains_anagrams(s):
    return len(s) >= 2 and len(s[0]) >= 3 and len(s[1]) >= 3 and sum(s[0] == s[i] for i in range(1, len(s) - 1)) >= 79
