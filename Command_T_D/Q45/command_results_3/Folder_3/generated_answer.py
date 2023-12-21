import re
def palindromes_between_indices(s):
    for m in re.finditer(r'([A-Z]+)([A-Z]+)([A-Z]+)', s):
        yield m.group(1) + m.group(2) + m.group(3)
