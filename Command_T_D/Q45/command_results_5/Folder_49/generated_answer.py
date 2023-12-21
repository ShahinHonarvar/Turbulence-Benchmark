import re
def palindromes_between_indices(str):
    s = list(str)
    return set(re.findall(r"([a-z]+)([A-Z][a-z]?)([a-z]?)\1", s[5:-2:-2]))
