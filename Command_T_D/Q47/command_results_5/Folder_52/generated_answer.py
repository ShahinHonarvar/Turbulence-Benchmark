import re
def palindromes_of_specific_lengths(s):
    return {m.group() for m in re.finditer(r'[a-z]{13,42}|[a-z]{44,99}', s, flags=re.I)}
