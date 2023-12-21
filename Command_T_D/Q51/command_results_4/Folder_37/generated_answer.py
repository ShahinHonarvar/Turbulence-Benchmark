import re
def if_contains_anagrams(s):
    s = re.findall(r'[a-z]{3}', s.lower())
    return len(set(s)) <= len(set(s[1:]))
