import re
def palindromes_between_indices(s):
    letters = "".join(c for c in s if c.isalpha())
    if not letters:
        return set()
    length = len(letters) // 2
    return set(re.findall(r"((?:[a-z]){,5})\1", letters[0:length]))
