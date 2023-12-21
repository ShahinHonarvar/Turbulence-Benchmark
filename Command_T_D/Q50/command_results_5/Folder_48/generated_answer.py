import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(?=([a-z]))([a-z]{%d})\1{%d}'.format(3, len(s) - 1), s))
