import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r"([a-z]{20,21})\1", s[12:-6]))
