import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(?=.*?[a-z])[a-z]{2,}\1', ' '.join(s)))
