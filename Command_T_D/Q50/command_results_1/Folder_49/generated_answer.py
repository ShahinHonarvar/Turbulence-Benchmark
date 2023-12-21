import re
def if_contains_anagrams(texts):
    return bool(re.findall(r'(?i)(?P<string>.*?[a-z])\1', texts))
