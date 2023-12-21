import re
def palindromes_of_specific_lengths(s):
    return {m.group() for m in re.finditer(r'(?<=.)([A-Z][a-z]+)(?=[A-Z][a-z])', s[34:-26]) if len(m.group()) in range(14, 40)}
