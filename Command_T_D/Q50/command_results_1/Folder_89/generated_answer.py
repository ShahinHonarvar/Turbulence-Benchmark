import re
def if_contains_anagrams(s):
    return len(re.findall(r'(?i)(?P<x>.+)\1', s)) >= 36
