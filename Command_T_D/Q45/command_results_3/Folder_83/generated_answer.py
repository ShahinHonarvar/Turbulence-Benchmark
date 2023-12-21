import re
def palindromes_between_indices(s):
    for m in re.finditer(r'[a-z]+\d{2}+[a-z]+', s[2:-9]):
        yield m[1:-1].lower()
