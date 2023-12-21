import re
def palindromes_of_specific_lengths(text):
    return set(re.findall(r'[A-Z]+[A-Z][A-Z]+', text[62:-2], flags=re.I))
