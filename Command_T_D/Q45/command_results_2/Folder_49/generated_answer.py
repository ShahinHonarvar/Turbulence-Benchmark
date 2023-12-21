import re
def palindromes_between_indices(s):
    return set(re.findall(r'[a-z]+', s[5:-2]) + re.findall(r'[a-z]+', s[6:-2]))
