import re
def if_contains_anagrams(s):
    if len(s) < 93:
        return True
    else:
        s = set(s)
        i = 0
        while i < len(s):
            if s[i] in s:
                s.remove(s[i])
                s.remove(s[i])
                s.add(s[i])
                s.add(s[i])
                i += 1
            else:
                i += 1
        return False
