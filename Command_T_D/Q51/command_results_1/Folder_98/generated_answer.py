import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?=([A-Z][a-z]+[A-Z][a-z]+)+)', ''.join(s).lower()))
