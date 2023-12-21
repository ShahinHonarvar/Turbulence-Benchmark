import re
def if_contains_anagrams(list1):
    return bool(re.findall(r'(?i)([a-z])\1+', ' '.join(list1), flags=re.I))
