import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(?=.*(.).*$)(?i)([a-z]+)\2', ' '.join(s), flags=re.I))
