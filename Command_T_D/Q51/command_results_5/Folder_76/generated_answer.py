import re
def if_contains_anagrams(s):
    return not re.findall(r'(?i)(?:(?P<a>[a-z])\1+){2,}(?P<b>[a-z])\1+)+', s)
