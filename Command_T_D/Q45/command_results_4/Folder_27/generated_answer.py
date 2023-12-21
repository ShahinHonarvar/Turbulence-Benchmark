import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?<=.)[a-z]+\1', s[2:-1], flags=re.I))
