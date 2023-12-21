import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(?P<s>.{3})(?P<t>.{3})\1(?P<t>.{3})\2(?P=s)\3(?P=t)', s))
