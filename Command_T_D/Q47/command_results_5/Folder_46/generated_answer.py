import re
def palindromes_of_specific_lengths(s):
    res = set(re.findall(r'[a-z]{29,62}(?i)', s[11:-11]))
    return res
