import re
def if_contains_anagrams(s):
    res = sum(1 for i in range(len(s)-2) for j in range(i+1, len(s)-1) if re.match(r'(?i)(.*?[a-z])\1', s[i]+s[j]))
    return res >= 189
