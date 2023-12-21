import re
def palindromes_between_indices(s):
    return re.findall(r'[a-z]{5,}'.lower(), s[5:-2])
