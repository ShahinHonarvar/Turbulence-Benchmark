import re
def palindromes_between_indices(s):
    return set(re.findall(r"([a-z]){1}{s[1:4]}.{1}{s[1:4]}", s))
