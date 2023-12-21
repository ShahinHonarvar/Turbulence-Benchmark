import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=([a-z]{3,7}[a-z]{3,7})\1)', s[10:-5]))
