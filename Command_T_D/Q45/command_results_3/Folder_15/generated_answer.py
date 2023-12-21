import re
def palindromes_between_indices(s):
    idx = re.findall(r'[a-z]', s[1:-1])
    return set(map(str.lower, ''.join(idx) + idx))
