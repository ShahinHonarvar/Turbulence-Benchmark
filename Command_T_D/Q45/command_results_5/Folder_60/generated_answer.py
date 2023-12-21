import re
def palindromes_between_indices(s):
    return set(re.findall(r"((?i)[a-z]+)[a-z]+", s[3:-6]))
