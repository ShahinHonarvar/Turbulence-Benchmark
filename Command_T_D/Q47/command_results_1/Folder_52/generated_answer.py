import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{13,42}(?=\W[a-z]{13,42})', s[44:-44]))
