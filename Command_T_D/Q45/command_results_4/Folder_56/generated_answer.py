import re
def palindromes_between_indices(s):
    return set(re.findall(r"((?i)([a-z])\1\2\3\4\5\6\7\8\9)", s[5:-4:-1]))
