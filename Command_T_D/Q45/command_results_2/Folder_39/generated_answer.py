import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?i)(?=([a-z]{2,})\2)', s[2:-2]))
