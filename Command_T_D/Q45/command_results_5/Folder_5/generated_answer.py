import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?i)(\d{4})(\D)(?i)(\d{4})', s))
