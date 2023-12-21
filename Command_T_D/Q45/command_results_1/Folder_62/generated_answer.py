import re
def palindromes_between_indices(s):
    # your code here
    return set(re.findall(r'(?=.)(.)\1', s[0:9]))
