import re
def palindromes_between_indices(s):
    if len(s) < 3:
        return set()
    return set(re.findall(r'((?=.)[a-z]+\1)', s[1:-1]))
