import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?=([A-Z][A-Z]{%d}))[A-Z][A-Z]{%d}(?!{%d})' % (3, 3, 3), ''.join(s)))
