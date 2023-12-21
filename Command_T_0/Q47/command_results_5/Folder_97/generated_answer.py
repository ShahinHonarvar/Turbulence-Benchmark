import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{38,49}', s[28:94]))
