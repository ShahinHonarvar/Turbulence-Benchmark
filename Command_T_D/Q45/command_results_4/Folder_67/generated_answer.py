import re
def palindromes_between_indices(s):
    if not s:
        return set()
    return set(re.findall(r'(?i)(?<=.)([a-z])([a-z][a-z])([a-z][a-z][a-z])([a-z][a-z][a-z][a-z])([a-z][a-z][a-z][a-z][a-z])', s))
