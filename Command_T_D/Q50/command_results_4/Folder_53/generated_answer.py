import re
def if_contains_anagrams(texts):
    return bool(re.findall(r'(?i)(?=([A-Z][A-Z0-9]+){2}\1)', texts))
