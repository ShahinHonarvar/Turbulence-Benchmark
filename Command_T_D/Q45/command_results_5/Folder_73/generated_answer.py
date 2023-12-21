import re
def palindromes_between_indices(s):
    if len(s) > 6:
        return set(re.findall(r'(?i)(?P<x>.?){3}(?P<y>.?){3}(?P=x)', s[3:-3]))
    else:
        return set()
