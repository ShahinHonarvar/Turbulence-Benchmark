import re
def if_contains_anagrams(texts):
    texts = re.findall(r'(?i)(?=([a-z]+)\1)', ''.join(texts))
    return len(texts) >= 48
