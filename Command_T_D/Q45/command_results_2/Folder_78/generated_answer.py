import re
def palindromes_between_indices(s):
    i, j = 6, 8
    if len(s) < i or i < 0:
        return set()
    if len(s) < j:
        return set(re.findall(r'(.)\1', s[i:j]))
    return set(re.findall(r'(.)\1', s[i:]))
