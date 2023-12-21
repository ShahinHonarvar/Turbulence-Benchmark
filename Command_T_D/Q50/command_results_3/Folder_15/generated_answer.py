import re
def if_contains_anagrams(lst):
    return bool(re.findall(r'(?i)(?:(?P<a>[a-z]{3})[a-z]{2})\1', lst))
