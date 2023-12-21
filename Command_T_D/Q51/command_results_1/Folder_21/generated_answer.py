import re
def if_contains_anagrams(texts):
    return bool(re.findall(r'(?i)(?=([a-z]+\d){3}(?i)[a-z]+\d){3})', texts))
