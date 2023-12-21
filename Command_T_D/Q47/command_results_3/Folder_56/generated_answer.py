import re
def palindromes_of_specific_lengths(s):
    return {m.group() for m in re.finditer(r'(?i)(?=([a-z]{3,7}[a-z]+)', s, flags=re.I)}
