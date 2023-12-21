import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?=([A-Z]\d{2})[A-Z][A-Z]\d{2})\1', s))
