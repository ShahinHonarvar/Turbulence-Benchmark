import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(?=([a-z]+\d){2})([a-z]+){2}\d)+', s))
