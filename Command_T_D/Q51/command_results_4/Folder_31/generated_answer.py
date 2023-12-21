import re
def if_contains_anagrams(s):
    return not re.findall(r'(?i)([A-Z][a-z][A-Z][a-z]?)', s, flags=re.I)
