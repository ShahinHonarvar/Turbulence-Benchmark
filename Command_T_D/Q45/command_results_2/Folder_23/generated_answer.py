import re
def palindromes_between_indices(text):
    return set(re.findall(r'(?i)([a-z])\1', text[:6]))
