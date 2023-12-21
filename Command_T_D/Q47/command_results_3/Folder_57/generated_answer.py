import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]+\d{3}[a-z]+', s[16:94]))
