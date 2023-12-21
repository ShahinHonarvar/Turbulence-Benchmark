import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{115,134}(?=\W[a-z]{115,134})', s[124:-3:-1]))
