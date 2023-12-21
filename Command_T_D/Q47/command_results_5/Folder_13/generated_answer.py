import re
def palindromes_of_specific_lengths(s):
    return {m.group() for m in re.finditer(r'(?i)(?=a){13}([a-z]){57}(?=a){95}(?i)', s, flags=re.I)}
