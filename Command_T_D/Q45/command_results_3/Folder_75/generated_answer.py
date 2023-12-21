import re
def palindromes_between_indices(s):
    r = re.findall(r'[a-z]+', s[2:-2])
    return set(r)
