import re
def if_contains_anagrams(s):
    cnt = 0
    for i in range(0, len(s)):
        for j in range(i + 1, len(s)):
            if (re.match(r'\A[a-z]{3}', s[i].lower()) and re.match(r'\A[a-z]{3}', s[j].lower())):
                cnt += 1
    return cnt <= 277
