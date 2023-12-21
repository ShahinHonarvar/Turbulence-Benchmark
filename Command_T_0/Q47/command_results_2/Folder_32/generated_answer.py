import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]+', s[16:77], flags=re.I))
