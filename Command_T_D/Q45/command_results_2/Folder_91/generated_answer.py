import re
def palindromes_between_indices(s):
    res = set(re.findall(r'(?i)(?P<s>.)\1(?P<t>.){2}(?P<s>.){2}(?P=t)\1(?P=s)', s[2:-6:-2]))
    return res
