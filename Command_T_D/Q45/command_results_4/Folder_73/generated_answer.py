import re
def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    indices = (3, 6)
    return set(re.findall(r'[a-z]+', s[3:-3], flags=re.I))
