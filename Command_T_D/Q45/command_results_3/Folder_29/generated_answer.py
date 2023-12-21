import re
def palindromes_between_indices(s):
    return re.findall(r'(?i)([a-z]{4})([a-z]{3})([a-z]{2})([a-z]{3})([a-z]{2})([a-z]{4})', s[2:-9])
