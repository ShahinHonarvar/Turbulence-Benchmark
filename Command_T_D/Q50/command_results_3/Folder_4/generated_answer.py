import re
def if_contains_anagrams(text):
    res = len(re.findall(r'(?i)(?P<x>[A-Z][^A-Z]?)\1', text)) >= 42
    return res
