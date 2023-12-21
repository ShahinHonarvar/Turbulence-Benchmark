import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?P<s>[a-z]{24,52})\1', s[10:-10], flags=re.I))
