import re
def if_contains_anagrams(texts):
    return len(re.findall(r"(\A[a-z]+[A-Z][a-z]?)\1", texts)) <= 25
