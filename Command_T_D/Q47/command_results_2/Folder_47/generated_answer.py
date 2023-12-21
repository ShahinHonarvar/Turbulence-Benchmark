import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=([a-z])\1)', s[39:-94]))
