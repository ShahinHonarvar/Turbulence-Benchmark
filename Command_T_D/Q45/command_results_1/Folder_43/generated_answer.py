import re
def palindromes_between_indices(s):
    for m in re.finditer(r'([a-z])?([a-z]?)([a-z]?)([a-z]?)([a-z]?)', s[2:-5]):
        yield m.group(2).lower() + m.group(3).lower() + m.group(4).lower() + m.group(5).lower()
