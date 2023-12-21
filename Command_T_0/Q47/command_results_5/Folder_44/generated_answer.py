import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{31,51}(?=\W|$)', s[18:-98]))
