import re
def palindromes_of_specific_lengths(s):
    return {m.group() for m in re.finditer(r'[a-z]{3,60}|(?i)[a-z]{3,60}'.lower(), s[70:-70])}
