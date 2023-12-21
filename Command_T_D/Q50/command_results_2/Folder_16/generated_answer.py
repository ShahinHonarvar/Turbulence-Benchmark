import re
def if_contains_anagrams(texts):
    res = re.findall(r'(?=([a-z0-9]+)\1)', texts, flags=re.I)
    return len(res) >= 155
