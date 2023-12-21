import re
def palindromes_between_indices(text):
    return set(re.findall(r'[a-z]+', text[1:-1], flags=re.I))
