import re
def palindromes_of_specific_lengths(text):
    return set(re.findall(r'(?i)([a-z]{18,36})\1', text[10:59]))
