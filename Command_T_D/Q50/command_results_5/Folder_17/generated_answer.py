import re
def if_contains_anagrams(s):
    return bool(re.findall(r'(?i)(?P<a>.{3})(?P<b>.{3})(?P<aub>.{3})(?P<au>.{3})(?P<bub>.{3})(?P<aubub>.{3})(?P<auub>.{3})(?P<bubub>.{3})', s))
