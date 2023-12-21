import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{14,39}(?=\w)', s[34:-90]))
