import re
def palindromes_of_specific_lengths(s):
    patterns = [re.compile(r'(?i)(?P<![a-z])[a-z]{2}(?![a-z])', flags=re.I)]
    return {m.group() for m in patterns if m.group(0) in s[0:10]]
