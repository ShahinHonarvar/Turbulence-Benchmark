import re
def if_contains_anagrams(s):
    s = sorted(set(s))
    cnt = 0
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if(re.match(r'(?i)(?P<a>[a-z]+){2}(?P<b>[a-z]+){2}', s[i]) and re.match(r'(?i)(?P<a>[a-z]+){2}(?P<b>[a-z]+){2}', s[j])):
                cnt += 1
    return cnt >= 24
