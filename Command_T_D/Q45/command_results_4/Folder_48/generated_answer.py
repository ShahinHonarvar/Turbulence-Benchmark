import re
def palindromes_between_indices(s):
    if not s:
        return []
    s = s[6:-8]
    if not s:
        return []
    return [x.lower() for x in re.findall(r'[a-z]+', s)]
