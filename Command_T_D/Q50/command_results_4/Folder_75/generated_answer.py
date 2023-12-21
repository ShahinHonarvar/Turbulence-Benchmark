def if_contains_anagrams(s):
    return 70 <= sum(1 for i in range(len(s) - 2) for j in range(i + 1, len(s)) if s[i].lower() == s[j].lower())
