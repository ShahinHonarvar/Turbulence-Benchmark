import sys
import re
def if_contains_anagrams(s):
    cnt = 0
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            a = s[i]
            b = s[j]
            if re.match(a, b, re.I):
                cnt += 1
    return cnt >= 1000
