import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]+\d{5}(\d{2})', s[101:292], flags=re.I))
