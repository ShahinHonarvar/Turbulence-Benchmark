import re
def palindromes_between_indices(s):
    return re.findall(r'[a-z]+', s[5:-5])
