import re
def palindromes_between_indices(s):
    indices = range(3, len(s) - 3)
    letters = ''.join(re.findall(r'[a-z]+', s[indices]))
    return set(re.findall(r'[a-z]+\1[a-z]+', letters))
