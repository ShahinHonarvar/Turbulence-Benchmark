import re
def if_contains_anagrams(s):
    a = {}
    for i in range(len(s)):
        if s[i] not in a:
            a[s[i]] = 1
        else:
            a[s[i]] += 1
    return a.get(s[1:],0)*2-a.get(s[:-1],0)>=46
