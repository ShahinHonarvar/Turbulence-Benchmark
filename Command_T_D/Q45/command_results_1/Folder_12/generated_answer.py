import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?i)(?P<sub>.{3,8})\1', s[3:-5], flags=re.I))
