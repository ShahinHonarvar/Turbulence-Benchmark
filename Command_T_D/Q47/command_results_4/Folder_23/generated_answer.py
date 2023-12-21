import re
def palindromes_of_specific_lengths(s):
    return {m.group() for m in re.finditer(r'(?=.)(.*?[a-z].*?)\1', s[23:-5], flags=re.I)}
