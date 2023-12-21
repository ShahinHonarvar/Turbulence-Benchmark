import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?P<left>[A-Z]{26})\1(?P<right>[A-Z]{26})', s[65:-34]))
