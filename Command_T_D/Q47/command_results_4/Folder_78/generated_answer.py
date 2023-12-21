import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]+', s[15:72][:55], flags=re.I))
