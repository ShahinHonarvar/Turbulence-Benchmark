import re
def palindromes_between_indices(s):
    if not s:
        return set()
    else:
        return set(re.findall(r'(?=.)(.)\1', s[3:-4].lower()))
