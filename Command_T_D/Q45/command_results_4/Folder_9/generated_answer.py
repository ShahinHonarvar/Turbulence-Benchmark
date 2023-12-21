import re
def palindromes_between_indices(s):
    s = s.lower()
    return {m[0] for m in re.finditer(r'(.)?([a-z])([a-z].){5}(?=\2)', s)}
