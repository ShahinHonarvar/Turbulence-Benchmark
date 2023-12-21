import re
def if_contains_anagrams(text):
    return bool(re.findall(r'(?i)(?:[a-z]+){3}+(?:[a-z]+){3}', text))
