import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{26,29}', s[13:99]))
