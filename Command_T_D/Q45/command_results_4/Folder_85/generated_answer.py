import re
def palindromes_between_indices(s):
    return set(re.findall(r'[a-z]+', s[2:-1])[::-1])
