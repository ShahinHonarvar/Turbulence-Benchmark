import re
def palindromes_of_specific_lengths(s):
    return {m.group() for m in re.finditer(r"<(.*?)>", s, flags=re.I)}
