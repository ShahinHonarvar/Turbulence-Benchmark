import re
def palindromes_between_indices(s):
    return set(re.findall(r"([A-Z]+)([a-z]+)([A-Z]+)", s))
