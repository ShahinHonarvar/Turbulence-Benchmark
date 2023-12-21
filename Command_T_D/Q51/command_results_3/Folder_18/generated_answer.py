import re
def if_contains_anagrams(texts):
    return bool(re.findall(r'(?i)(?:[a-z]){2}([a-z]){3}([a-z]){2}', texts))
