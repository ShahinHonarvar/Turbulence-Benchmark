import re
def if_contains_anagrams(texts):
    return bool(re.findall(r'\A[A-Z][^A-Z]*[A-Z][^A-Z]*[A-Z][^A-Z]*\Z', texts, flags=re.I))
