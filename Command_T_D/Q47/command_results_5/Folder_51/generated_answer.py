import re
def palindromes_of_specific_lengths(text):
    return set(re.findall(r'(?i)(?=([a-z]){3}[a-z]{2}))[a-z]{3}[a-z]{2}(?=([a-z]){3}[a-z]{2})', text[2:-8]))
