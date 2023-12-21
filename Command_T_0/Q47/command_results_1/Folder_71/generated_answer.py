import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{23,36}'.lower(), s[18:65]))
