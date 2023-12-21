import re
def palindromes_between_indices(strng):
    strng = strng[2:-5]
    return set(re.findall(r'[a-z]+', strng.lower()))
