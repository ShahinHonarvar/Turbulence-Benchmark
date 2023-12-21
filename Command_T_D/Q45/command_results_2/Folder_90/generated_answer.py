import re
def palindromes_between_indices(s):
    letters = re.findall("[a-z]", s)
    if len(letters) < 4:
        return set()
    return set(x for x in s[0:6] if str(x)[::-1] == str(x))
