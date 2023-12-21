import re
def if_contains_anagrams(s):
    cnt = 0
    for i in range(len(s) - 2):
        for j in range(i + 1, len(s) - 1):
            s1 = s[i].lower()
            s2 = s[j].lower()
            if re.match(s1, s2):
                cnt += 1
    return cnt >= 29
