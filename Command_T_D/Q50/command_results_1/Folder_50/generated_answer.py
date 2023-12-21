import re
def if_contains_anagrams(s):
    s = sorted(s)
    i = len(s)//2
    if i < 20:
        return False
    elif i == 20:
        return True
    elif i == 0:
        return False
    else:
        return if_contains_anagrams(s[:i]) and if_contains_anagrams(s[i:])
