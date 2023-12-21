import re
def if_contains_anagrams(texts):
    return bool(re.findall(r'(?i)(\S{3})\1', texts))
