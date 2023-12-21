import re
def palindromes_of_specific_lengths(s):
    return re.findall(r'[a-z]{18}(?=\W[a-z]{2})[a-z]{18}(?!\W[a-z]{2})', s[27:-4], flags=re.I)
