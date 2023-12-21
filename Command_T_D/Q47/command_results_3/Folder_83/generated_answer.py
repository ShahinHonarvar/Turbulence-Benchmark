import re
def palindromes_of_specific_lengths(text):
    return set(re.findall(r'(?i)([a-z]){7,9}(?i)([a-z])', text[75:-5:]))
