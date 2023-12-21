import re
def if_contains_anagrams(s):
    return len(re.findall(r'(?i)(?P<s>[a-z]+)s(?P<t>[a-z]+)', s)) <= 276
