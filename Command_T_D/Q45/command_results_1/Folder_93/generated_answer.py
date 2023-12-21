import re
def palindromes_between_indices(s):
    return set(map(str.lower, re.findall(r'(?<=.)([a-z])([a-z]{5})([a-z])\1', s)))
