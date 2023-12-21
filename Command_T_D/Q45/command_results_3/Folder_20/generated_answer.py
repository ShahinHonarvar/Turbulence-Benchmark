import re
def palindromes_between_indices(s):
    if not s:
        return []
    s = s[2:-8]
    return [x for x in re.findall(r'((?i)[a-z]){4}(?i)[a-z]'.format(4), s)]
