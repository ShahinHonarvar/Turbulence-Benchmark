import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=([a-z]){52})([a-z]){52}(?=[a-z]{87}[a-z]{26})', s))
