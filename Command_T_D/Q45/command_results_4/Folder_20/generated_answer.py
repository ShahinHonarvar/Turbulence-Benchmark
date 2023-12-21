import re
def palindromes_between_indices(s):
    for m in re.finditer(r'(.*?[a-z])(.*?[A-Z])(.*?[a-z])(.*?[A-Z])(.*?[a-z])(.*?[A-Z])(.*?[a-z])', s):
        yield m.group()
