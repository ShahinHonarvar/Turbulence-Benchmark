import re
def palindromes_between_indices(text):
    for m in re.finditer(r'[a-z]{4}', text):
        yield m.group()
