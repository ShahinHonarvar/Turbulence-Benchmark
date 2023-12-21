import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?=([a-z]+[A-Z][a-z]?)[a-z]+[A-Z][a-z]?)[a-z]+[A-Z][a-z]?)', s))
