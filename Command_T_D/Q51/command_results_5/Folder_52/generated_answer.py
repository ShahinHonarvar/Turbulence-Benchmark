import re
def if_contains_anagrams(texts):
    return bool(re.findall(r'(?i)(?=([a-z]+)\1)', ''.join(map(str.lower, texts))))
