import re
def palindromes_between_indices(s):
    indices = range(0,8)
    letters = set(re.findall(r'[a-z]', s[0:8]))
    return set(x for x in s[0:8] if x[::-1] in letters)
