import re
def palindromes_of_specific_lengths(text):
    return set(re.findall(r'[a-z]+', text[12:92:2], flags=re.I))
