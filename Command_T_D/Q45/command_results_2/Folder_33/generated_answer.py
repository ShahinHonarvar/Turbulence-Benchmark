import re
def palindromes_between_indices(s):
    if len(s) < 7:
        return set()
    return set(re.findall(r'[a-z]+', s[7:-9]))
