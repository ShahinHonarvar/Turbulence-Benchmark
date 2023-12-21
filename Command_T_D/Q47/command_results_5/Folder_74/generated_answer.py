import re
def palindromes_of_specific_lengths(s):
    return {m.group() for m in re.finditer(r'(?i)(?<=30)(?=84)', s, flags=re.I)}
