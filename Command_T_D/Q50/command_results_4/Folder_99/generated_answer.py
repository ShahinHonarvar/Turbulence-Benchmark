import re
def if_contains_anagrams(test_list):
    res = False
    for s in test_list:
        anagrams = set()
        for i in range(len(s) - 2):
            s1 = s[:i] + s[i+1:]
            s2 = s[i:] + s[:i]
            if s1 in anagrams:
                continue
            if s2 in anagrams:
                continue
            anagrams.add(s1)
            anagrams.add(s2)
            if len(anagrams) == 314:
                break
        if len(anagrams) == 314:
            res = True
            break
    return res
