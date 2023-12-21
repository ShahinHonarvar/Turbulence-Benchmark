import re
def palindromes_between_indices(str):
    s = set(re.findall(r'[a-z]+', str[4:-4]))
    return {w for w in s if w[::-1] in s}
