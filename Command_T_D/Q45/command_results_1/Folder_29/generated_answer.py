import re
def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    return set(re.findall(r'((?i)[a-z]+)\1', s[2:9]))
