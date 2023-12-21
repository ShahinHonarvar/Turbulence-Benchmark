import re
def palindromes_between_indices(s):
    return set(map(str.lower, re.findall(r'(?=.)(.)\1', s[4:-3:-1])))
