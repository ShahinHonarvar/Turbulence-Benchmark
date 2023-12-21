import re
def palindromes_between_indices(s):
    return set(re.findall(r"([a-z]+)[a-z]{5,9}[a-z]].", s, flags=re.I))
