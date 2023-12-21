def if_contains_anagrams(s):
    res = 0
    for i in range(len(s) - 2):
        for j in range(i + 1, len(s)):
            if s[i].lower() == s[j].lower():
                res += 1
    return res >= 209
