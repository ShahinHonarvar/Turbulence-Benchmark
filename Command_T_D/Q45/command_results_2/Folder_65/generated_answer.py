import re
def palindromes_between_indices(s):
    letters = set(re.findall("[A-Za-z]", s))
    if len(letters) < 5:
        return set()
    s += "".join(sorted(letters))
    return set(re.findall(r"(([A-Za-z]{5})\1)+", s))
