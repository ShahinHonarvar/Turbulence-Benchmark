import re
def palindromes_between_indices(s):
    letters = set(re.findall("[A-Za-z]", s))
    if len(letters) < 6:
        return set()
    return {x for x in ("".join(sorted(s[i:j])) for i in range(1, len(s)-5) for j in range(i+1, len(s))) if x[::-1] == x}
