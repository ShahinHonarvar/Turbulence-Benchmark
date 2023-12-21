import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?i)(?P<1>[a-z])\1(?P<2>[a-z])\2(?P=1)(?P=2)', s[5:-8]))
