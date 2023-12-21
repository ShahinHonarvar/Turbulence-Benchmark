import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{26}(?:[a-z]{1})', s[33:-1]))
