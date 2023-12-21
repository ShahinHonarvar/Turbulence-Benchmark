import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?=([a-z]){6}([a-z]){4}([a-z]){6})', s))
