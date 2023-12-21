import re
def palindrome_of_length_n(s):
    return {m.group() for m in RE.finditer(s, flags=re.I)}
