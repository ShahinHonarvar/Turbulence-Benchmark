import re
def palindromes_between_indices(s):
    for m in re.finditer(r'[a-z]{4}(?=[a-z0-9])', s):
        yield m.group()
