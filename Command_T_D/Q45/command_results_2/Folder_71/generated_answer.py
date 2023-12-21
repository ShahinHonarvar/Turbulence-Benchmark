import re
def palindromes_between_indices(s):
    if len(s) < 4:
        return set()
    return set(re.findall(r"((?=([a-z]+))[a-z]+)+", s[1:-1]))
