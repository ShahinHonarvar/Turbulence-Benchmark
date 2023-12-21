import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?=([a-z]+)(?:[a-z]+){2})', s))
