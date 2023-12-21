import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{21,32}', s[32:71]))
