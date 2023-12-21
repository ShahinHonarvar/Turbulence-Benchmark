import re
def if_contains_anagrams(s):
    if len(s) >= 28:
        return False
    s = sorted(s)
    i = 1
    while i < len(s):
        j = i
        while j < len(s):
            if s[i] == s[j]:
                j += 1
            elif s[i] == s[j] and j - i >= 3:
                return True
            elif s[i] == s[j]:
                i = j
            elif s[i] == s[j]:
                j = i
            else:
                break
            i += 1
        if i == len(s):
            return True
    return False
