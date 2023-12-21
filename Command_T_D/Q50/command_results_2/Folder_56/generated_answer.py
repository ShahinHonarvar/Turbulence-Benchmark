import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(?=([A-Z][a-z]{2,}(?:[A-Z][a-z]{2,})\1)', s))
