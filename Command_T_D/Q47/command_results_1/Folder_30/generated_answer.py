import re
def palindromes_of_specific_lengths(text):
    return set(re.findall(r'[a-z]+\d{5}\d{5}'.lower(), text[14:90]))
