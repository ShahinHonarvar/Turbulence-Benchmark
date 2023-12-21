import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]+[a-z]+[a-z]+[a-z]+[a-z]+[a-z]+', s[40:94]))
