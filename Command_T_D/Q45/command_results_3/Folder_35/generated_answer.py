import re
def palindromes_between_indices(s):
    return set(re.findall(r'[a-z]+\d+[a-z]+', s[2:-4], flags=re.I))
