import re
def palindromes_between_indices(s):
    a, b = 4, 8
    r = re.findall(r'[a-z]', s[a:b])
    return set(r + r[::-1])
