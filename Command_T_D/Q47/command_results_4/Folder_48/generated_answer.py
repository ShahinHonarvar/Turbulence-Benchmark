import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[A-Z]+', s[155:-4:-1], flags=re.I))
