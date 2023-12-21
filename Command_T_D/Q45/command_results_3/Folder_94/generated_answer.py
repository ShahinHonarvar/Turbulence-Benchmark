import re
def palindromes_between_indices(s):
    r = re.findall(r'([a-z]+[A-Z][a-z]+)', s[3:-4])
    return set(r)
