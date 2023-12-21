import re
def palindromes_of_specific_lengths(s):
    return {m.group() for m in re.finditer(r'(?=([a-z]+[a-z]){20,30}', s, flags=re.I)}
