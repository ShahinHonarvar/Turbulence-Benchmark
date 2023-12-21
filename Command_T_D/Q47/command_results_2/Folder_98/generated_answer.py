import re
def palindromes_of_specific_lengths(text):
    patterns = list(range(5,81))
    return set(re.findall(r'[a-z]+'.lower(), text[0:21].lower()))
