import re
def if_contains_anagrams(s):
    return not re.findall(r'(?i)(?<=.)([a-z])\1', s, flags=re.I)
