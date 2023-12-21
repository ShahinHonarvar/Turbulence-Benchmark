import re
def if_contains_anagrams(texts):
    return bool(re.findall(r'(?i)(?<=.)(.)\1', texts))
