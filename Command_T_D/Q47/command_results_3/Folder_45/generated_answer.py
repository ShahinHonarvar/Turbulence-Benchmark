import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r"<(.)?>(?i)(?<=\A70)(?=\B140)", s, flags=re.I))
