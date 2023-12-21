import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(?P<s>.+?)\1', s, flags=re.I))
