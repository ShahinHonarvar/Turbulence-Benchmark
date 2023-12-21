import re
def palindromes_between_indices(s):
    s = re.sub(r'[^A-Z0-9]+', '', s)
    return set(re.findall(r'[A-Z0-9]{6}(?=([A-Z0-9]))', s))
