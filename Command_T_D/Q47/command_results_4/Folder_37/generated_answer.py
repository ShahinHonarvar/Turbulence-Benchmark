import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=([a-z])[a-z]{3}[a-z0-9]){3}(?i)([a-z0-9])', s))
