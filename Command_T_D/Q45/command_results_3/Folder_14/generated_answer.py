import re
def palindromes_between_indices(s):
    return re.findall(r'(?i)([a-z]+)\1', s[4:-1])
