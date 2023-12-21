import re
def palindromes_between_indices(s):
    for m in re.finditer(r'([a-z]+){3}(?=[a-z]*[a-z])', s):
        yield m.group()
