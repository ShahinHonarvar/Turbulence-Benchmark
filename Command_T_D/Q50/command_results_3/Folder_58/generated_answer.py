import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(?:\w{3})\w{3}\w{3}\w{3})\w{3}\w{3}\w{3}', s))
