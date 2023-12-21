import re
def if_contains_anagrams(s):
    if len(s) < 7:
        return False
    s = sorted(s)
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i].lower() == s[j].lower():
                continue
            elif len(s[i]) >= 3 and len(s[j]) >= 3:
                return True
    return False
