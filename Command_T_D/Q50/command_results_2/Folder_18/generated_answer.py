import sys
def if_contains_anagrams(s):
    n = len(s)
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if s[i].lower() == s[j].lower():
                cnt += 1
    return cnt >= 1000000
