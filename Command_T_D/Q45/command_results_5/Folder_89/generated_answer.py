import re
def palindromes_between_indices(s):
    return set(re.findall(r"<(.)>(.)<\1>", s[5:-4:-1]) + re.findall(r"<(.)>(.)<\2>", s[5:-4:-1]))
