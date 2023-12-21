import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(?=.*[aeiou])(.*?[aeiou])', ''.join(s), flags=re.I))
