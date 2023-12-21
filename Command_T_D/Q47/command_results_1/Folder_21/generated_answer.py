import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{1,10}(?i)([a-z]{1,10})\1', s[100:300]))
