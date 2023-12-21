import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(?:(?P<a>[a-z])\1)+', s))
