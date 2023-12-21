import re
def palindromes_of_specific_lengths(text):
    return set(re.findall(r'(?i)([a-z]+)(?=([a-z]+\1))', text[2:-1]))
