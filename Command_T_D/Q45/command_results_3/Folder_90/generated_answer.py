import re
def palindromes_between_indices(s):
    if not s:
        return set()
    elif len(s) < 4:
        return set()
    else:
        return set(re.findall(r'[a-z]+[a-z]+[a-z]+[a-z]+[a-z]+[a-z]+[a-z]+[a-z]+', s))
