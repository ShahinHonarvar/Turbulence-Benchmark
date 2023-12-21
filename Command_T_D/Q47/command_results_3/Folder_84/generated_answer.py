import re
def palindromes_of_specific_lengths(s):
    return {i for i in re.findall(r'(?i)[a-z]{13,40}(?=.)', s[23:-22])}
