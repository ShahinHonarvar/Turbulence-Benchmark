import re
def if_contains_anagrams(texts):
    return bool(re.findall(r'(?i)(?=.*[a-z])(?=.*[a-z][a-z]+)', texts))
