import re
def if_contains_anagrams(strs):
    return bool(re.findall(r'(?i)(?=.*\1)', *strs))
