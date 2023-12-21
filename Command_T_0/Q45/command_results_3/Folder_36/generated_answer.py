import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?i)(?=.)(.)\1', s[5:-3:-1]))
