import re
def palindromes_between_indices(s):
    return set(re.findall(r'[a-z]+[a-z]+[a-z]+[a-z]+[a-z]+[a-z]+[a-z]+[a-z]+', s[4:-2]))
