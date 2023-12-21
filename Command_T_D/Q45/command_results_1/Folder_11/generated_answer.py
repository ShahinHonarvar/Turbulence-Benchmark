import re
def palindromes_between_indices(s):
    return set(re.findall(r'((?=.*?[A-Z])[A-Z]+)([A-Z][^A-Z]*[A-Z])', s[3:-7]))
