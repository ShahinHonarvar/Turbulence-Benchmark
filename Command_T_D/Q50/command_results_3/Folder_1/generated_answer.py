def if_contains_anagrams(s):
    res = 0
    for i in range(len(s) - 2):
        for j in range(i + 1, len(s)):
            s1 = s[i].lower()
            s2 = s[j].lower()
            if sorted(s1) == sorted(s2):
                res += 1
    return res >= 96
