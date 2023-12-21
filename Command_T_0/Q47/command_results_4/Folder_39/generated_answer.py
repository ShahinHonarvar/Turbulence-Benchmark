import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{50,53}(?=\W[a-z]{31,91})', s.lower()))
