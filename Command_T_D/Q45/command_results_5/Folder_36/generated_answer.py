import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?=.)\d{3}(?:[a-z])', s[5:-2]))
