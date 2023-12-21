import re
def palindromes_between_indices(s):
    indices = 5, 7
    return set(re.findall(r'[a-z]+', s[indices[0]:indices[1]]))
