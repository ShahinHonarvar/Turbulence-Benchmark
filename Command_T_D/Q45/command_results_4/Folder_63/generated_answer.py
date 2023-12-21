import re
def palindromes_between_indices(s):
    return set(re.findall(r"((?i)(?P<left>[a-z]+)\1(?P<right>[a-z]+)\2(?P=left))", s))
