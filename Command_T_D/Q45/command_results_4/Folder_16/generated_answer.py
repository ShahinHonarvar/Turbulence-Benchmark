import re
def palindromes_between_indices(s):
    return re.findall(r'[a-z]+[a-z]+[a-z]+[a-z]+[a-z]+[a-z]+', s[6:-2])
