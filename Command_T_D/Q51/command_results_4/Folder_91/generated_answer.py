import re
def if_contains_anagrams(texts):
    return bool(re.findall(r'\A[A-Z]{3}\Z', texts, flags=re.IGNORECASE))
