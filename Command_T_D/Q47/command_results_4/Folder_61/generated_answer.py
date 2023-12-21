import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r"<(.)[\d_]+(.)>", s, flags=re.I))
