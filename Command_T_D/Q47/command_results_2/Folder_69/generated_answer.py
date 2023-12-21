import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{45,52}', s[11:96], flags=re.I))
