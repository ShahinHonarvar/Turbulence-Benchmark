import re
def palindromes_between_indices(s):
    idx = [i for i, c in enumerate(re.findall(r'[A-Z]', s[4:9])) if c]
    return {c for c in s[4:9][idx[0]:idx[1]] if c.lower() in c}
