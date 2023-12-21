import re
def palindromes_between_indices(s):
    lst = re.findall(r'[a-z]+', s[7:-1])
    if not lst:
        return []
    return {w[::-1] for w in lst}
