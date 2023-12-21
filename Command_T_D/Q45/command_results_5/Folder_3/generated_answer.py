import re
def palindromes_between_indices(s):
    return set(re.findall(r'[a-z]{3,}(?=[A-Z][^A-Z]*[a-z][^a-z]*[A-Z])', s))
