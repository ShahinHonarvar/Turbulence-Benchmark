import re
def if_contains_anagrams(text):
    return bool(re.findall(r'\A[A-Z][^A-Z]*[A-Z]\Z', text.lower()))
