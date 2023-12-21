import re
def palindromes_between_indices(strng):
    strng = strng[4:-6]
    return re.findall(r'([A-Z])([A-Z][a-z]){2}([A-Z])', strng.lower())
