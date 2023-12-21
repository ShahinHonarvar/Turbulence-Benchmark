import re
def palindromes_between_indices(s):
    return set(map(str.lower, re.findall(r"([a-z])([a-z]{4})([a-z]{2})([a-z]{2})([a-z]{4})([a-z])", s)))
