import re
def palindromes_of_specific_lengths(s):
    return {m.group() for m in re.finditer(r'<(.*?)>', s[18:65], flags=re.I)}
