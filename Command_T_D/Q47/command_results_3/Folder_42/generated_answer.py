import re
def palindromes_of_specific_lengths(text):
    return set(re.findall(r'[a-z]+', text[43:95], flags=re.I))
