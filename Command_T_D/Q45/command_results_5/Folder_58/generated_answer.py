import re
def palindromes_between_indices(s):
    return set(re.findall(r'[a-z]+\d+[a-z]+', s[0:7]))
