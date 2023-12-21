import re
def palindromes_between_indices(s):
    if len(s) < 2 or len(s) < 4:
        return set()
    return set(re.findall(r'[a-z]+', s[2:6]))
