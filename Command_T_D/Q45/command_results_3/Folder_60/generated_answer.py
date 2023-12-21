import re
def palindromes_between_indices(s):
    return set(re.findall(r"([a-z]{2,4})\1", s[3:-3]))
