import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{35,41}(?i)([a-z]{35,41})', s[32:-1], flags=re.I))
