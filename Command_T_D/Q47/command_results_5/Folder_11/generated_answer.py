import re
def palindromes_of_specific_lengths(s):
    i = 24
    j = 97
    return {m.group() for m in re.finditer(r'((?i)[a-z]{10,36})\1', s[i:j+1])}
