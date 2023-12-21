import re
def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    else:
        return set(re.findall(r'[a-z]+', s[1:-1]))
