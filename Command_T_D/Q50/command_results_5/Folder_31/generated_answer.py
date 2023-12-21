import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(?P<text>[a-z]+)\1', s))
