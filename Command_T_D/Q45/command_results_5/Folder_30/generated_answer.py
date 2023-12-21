import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?i)(?:[a-z]{2,3})\1', s[0:5]))
