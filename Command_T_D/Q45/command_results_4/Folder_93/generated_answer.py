import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?<=.)(.)\1', s[2:-7:-1]))
