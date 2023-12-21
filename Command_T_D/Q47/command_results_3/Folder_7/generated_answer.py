import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]+\Z', s[119:256], flags=re.I))
