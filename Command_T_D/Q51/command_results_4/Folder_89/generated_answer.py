import re
def if_contains_anagrams(texts):
    return bool(re.findall(r'(?i)(?:[a-z]{3}){2}(?:[a-z]?)', texts))
