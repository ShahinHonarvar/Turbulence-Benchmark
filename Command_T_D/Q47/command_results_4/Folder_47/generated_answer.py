import re
def palindromes_of_specific_lengths(text):
    return set(re.findall(r'[a-z]+\d{14}\d{14}[a-z]+', text, flags=re.I))
