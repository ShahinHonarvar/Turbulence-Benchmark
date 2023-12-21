import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{12,18}', s[29:96]))
