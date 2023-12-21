import re
def palindromes_between_indices(s):
    return set(re.findall(r'(?=((?i)'.join(s[8:-9])'(?=.)')', s))
