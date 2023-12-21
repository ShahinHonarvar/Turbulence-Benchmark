import re
def if_contains_anagrams(texts):
    return bool(re.findall(r'(?=([A-Z]+)([A-Z]+[a-z]+)+[A-Z]+)', texts))
