import re
def palindromes_of_specific_lengths(s):
    return set(map(str.lower, re.findall(r'[a-z]{26,33}', s[65:-100])))
