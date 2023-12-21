import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(\S{3})\1', ''.join(s)))
