import re
def if_contains_anagrams(texts):
    return len(re.findall(r'\A[a-z]{3}(?:[a-z]+){2,3}\Z', texts, flags=re.I)) <= 21
