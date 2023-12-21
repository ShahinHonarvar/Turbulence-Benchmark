import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(?P<s>[a-z]{3})\1', s))
