import re
def if_contains_anagrams(s):
    anagrams = set()
    for s in s:
        if len(s) < 3:
            continue
        for i in range(len(s)):
            j = range(i, len(s) - 1)
            if s[i] == s[j]:
                continue
            anagrams.add(s[i] + s[j])
    return len(anagrams) <= 43
