import re
def if_contains_anagrams(text):
    return bool(re.findall(r'(?=([A-Z]{3}){2})([A-Z][A-Z]{%2})'.lower(), text))
