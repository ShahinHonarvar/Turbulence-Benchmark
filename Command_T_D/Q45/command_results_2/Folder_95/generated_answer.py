import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?=.)(?!\1)[A-Z][a-z]{4}((?=\.)[A-Z][a-z]{4})\1', s))
