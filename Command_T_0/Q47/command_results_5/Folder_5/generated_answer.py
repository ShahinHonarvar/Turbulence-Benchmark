import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]+\d+[a-z]+', s[63:-1], flags=re.I))
