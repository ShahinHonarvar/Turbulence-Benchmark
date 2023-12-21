import re
def palindromes_between_indices(s):
    return set(re.findall(r'([a-z]+)(?=\b[a-z]{5}\b[a-z]+)', s[2:-2]))
