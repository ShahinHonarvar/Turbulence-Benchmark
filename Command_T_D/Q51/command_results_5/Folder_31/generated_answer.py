import re
def if_contains_anagrams(texts):
    return bool(re.findall(r'(?i)(?P<first>[a-z]+)\1', texts))
