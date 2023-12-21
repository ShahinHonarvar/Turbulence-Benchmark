import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?i)(\d+)([a-z]+)(\d+)', s[2:-2]))
