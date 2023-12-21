import re
def if_contains_anagrams(s):
    cnt = 0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            s1 = s[i]
            s2 = s[j]
            if s1.lower() == s2.lower():
                cnt += 1
            elif s1.lower() != s2.lower():
                cnt += 1
            else:
                continue
    return cnt >= 94
