import re
def if_contains_anagrams(text):
    return bool(re.findall(r'\A[a-z]+\d+[a-z]+\d+\Z', text, flags=re.I))
