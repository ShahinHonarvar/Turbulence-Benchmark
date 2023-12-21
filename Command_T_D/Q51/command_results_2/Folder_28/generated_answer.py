import re
def if_contains_anagrams(s):
    if len(s) < 3:
        return False
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                continue
            elif s[i] == s[j] or s[i].lower() == s[j].lower():
                return False
    return True
