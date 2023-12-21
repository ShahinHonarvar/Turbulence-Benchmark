import re
def palindromes_between_indices(s):
    return re.findall(r'([a-z]){4}(?=[A-Z][a-z]){2}(?=[A-Z][a-z]){4}', s)
