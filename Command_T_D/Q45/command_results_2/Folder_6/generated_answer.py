import re
def palindromes_between_indices(s):
    s = re.sub(r'[^A-Z0-9]+', '', s)
    if not s:
        return set()
    return set(s[i:j] for i in range(0, 8) for j in range(i, 8))
