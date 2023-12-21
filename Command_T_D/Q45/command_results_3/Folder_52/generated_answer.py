import re
def palindromes_between_indices(s):
    if not s:
        return set()
    return set(re.findall(r"((?i)[a-z]{6,})", s[0:8]))
