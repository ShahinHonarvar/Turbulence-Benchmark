import re
def palindromes_between_indices(s):
    return set(re.findall(r'[a-z]+[A-Z][a-z]+[A-Z][a-z]+[a-z]+[A-Z][a-z]+[a-z]+', s[1:-1]))
