import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{10,36}(?=.)', s[24:-3]))
