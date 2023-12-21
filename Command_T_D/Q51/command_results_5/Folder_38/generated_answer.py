import re
def if_contains_anagrams(lst):
    return bool(re.findall(r'(?i)(?=([a-z]+[A-Z][a-z]*)\1)', lst))
