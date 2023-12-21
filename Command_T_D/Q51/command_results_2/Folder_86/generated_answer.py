import re
def if_contains_anagrams(s):
    return not bool(re.findall(r"<(.*?)>(?i)([a-z]{2,})<(.*?)>", s))
