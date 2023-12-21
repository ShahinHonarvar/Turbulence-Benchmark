import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(\w){2,}(?=\w\1)', s))
