import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{104,120}', s[155:283]))
