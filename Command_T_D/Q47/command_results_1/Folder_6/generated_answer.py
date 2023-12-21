import re
def palindromes_of_specific_lengths(s):
    if not s:
        return set()
    if len(s) < 45 or len(s) > 98:
        return set()
    for i in range(40, 47):
        if re.match(r"^[a-z]+[a-z]$", s[45:45 + i]):
            return set(s[45:45 + i])
    return set()
