import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?i)(?<=.)([a-z]){5}(?=.)([a-z])', s))
