import re
def if_contains_anagrams(texts):
    return bool(re.findall(r'(?i)(?P<a>.*?)(?P<b>.*?)\1', texts))
