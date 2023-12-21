import re
def palindromes_between_indices(s):
    return re.findall(r'[a-z]{3}([a-z]{2})([a-z]{2})[a-z]{3}', s, flags=re.I)
