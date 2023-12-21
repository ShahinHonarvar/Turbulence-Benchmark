import re
def palindromes_between_indices(s):
    return re.findall(r'(?i)([a-z])([a-z][a-z][a-z])([a-z])', s)
