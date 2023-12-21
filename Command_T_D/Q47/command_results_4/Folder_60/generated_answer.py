import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{32,34}(?=.)', s[23:-83]))
