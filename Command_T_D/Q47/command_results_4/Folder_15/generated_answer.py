import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]+[a-z]{2,5}', s[0:7], flags=re.I))
