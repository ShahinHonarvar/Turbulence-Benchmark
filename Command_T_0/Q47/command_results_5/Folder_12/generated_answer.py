import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]+\d+[a-z]+', s[62:-2], flags=re.I))
