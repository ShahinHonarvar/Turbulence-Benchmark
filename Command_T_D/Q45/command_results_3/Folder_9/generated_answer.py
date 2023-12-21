import re
def palindromes_between_indices(s):
    if not s:
        return set()
    return set(re.findall(r'[a-z]{7}|Z', s))
