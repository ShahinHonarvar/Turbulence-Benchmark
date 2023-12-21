import re
def if_contains_anagrams(lst):
    return bool(re.findall(r'(?=([A-Z]+[A-Z][A-Z]+)', ' '.join(map(str.lower, lst))))
