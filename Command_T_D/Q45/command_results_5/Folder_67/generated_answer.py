import re
def palindromes_between_indices(s):
    i = 2
    j = 6
    if i > len(s) or j > len(s):
        return set()
    m = re.match(r'(?i)([a-z])\1', s[i:j])
    if m:
        return set(m.group(1))
    return set()
