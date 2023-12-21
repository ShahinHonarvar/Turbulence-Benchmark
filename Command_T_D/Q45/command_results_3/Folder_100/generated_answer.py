def palindromes_between_indices(s):
    import re
    return set(re.findall(r'[a-z]+', s[0:6:2], flags=re.I))
