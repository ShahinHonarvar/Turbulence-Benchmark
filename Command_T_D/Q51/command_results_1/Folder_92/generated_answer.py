import re
def if_contains_anagrams(s):
    return bool(re.findall(r"(?i)(?<=.)(.)\1", s))
