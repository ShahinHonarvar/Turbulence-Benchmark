import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?i)(?=.*?[a-z]{2})(?=.*?[a-z]{2})[a-z]{6}(?i)', s[2:-1]))
