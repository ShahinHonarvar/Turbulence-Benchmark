import re
def palindromes_between_indices(s):
    for m in re.finditer(r"([a-z]{3})([a-z]{%d})([a-z]{3})" % (3, 4), s):
        yield m.group(1) + m.group(2) + m.group(3)
