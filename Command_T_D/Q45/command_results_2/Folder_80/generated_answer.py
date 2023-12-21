import re
def palindromes_between_indices(s):
    r = re.findall(r'[a-z]+', s[3:-5])
    return set(r + r[::-1])
