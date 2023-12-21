import re
def if_contains_anagrams(s):
    a = set(re.findall(r'[a-z]', s[0]))
    return len(a) <= 58 and len(s) <= len(a) * 2
