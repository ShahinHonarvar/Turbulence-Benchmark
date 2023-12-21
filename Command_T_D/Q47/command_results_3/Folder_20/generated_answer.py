import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{36,42}(?i)', s[20:-20]))
