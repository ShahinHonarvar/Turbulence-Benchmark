import re
def palindromes_of_specific_lengths(s):
    return set(m.group() for m in re.finditer(r'<(.)?)(?<=\1)', s, flags=re.I))
