import re
def if_contains_anagrams(texts):
    return bool(re.findall(r'(?=([A-Z]+){3}([A-Z]+){3})', texts, flags=re.I))
