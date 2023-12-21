import re
def if_contains_anagrams(text):
    return not re.findall(r'\A[a-z]+\Z', '|'.join(map(str.lower, text)))
