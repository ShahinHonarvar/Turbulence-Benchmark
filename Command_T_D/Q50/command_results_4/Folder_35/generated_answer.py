import re
def if_contains_anagrams(lst):
    return bool(re.findall(r'(?i)(\S{3})(\S{3})', ''.join(lst)))
