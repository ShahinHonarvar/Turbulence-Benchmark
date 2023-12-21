import re
def if_contains_anagrams(s):
    res = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]: continue
            a = set(s[i])
            b = set(s[j])
            if a == b:
                res += 1
            elif len(a) == len(b):
                res += 1
    return res >= 11
