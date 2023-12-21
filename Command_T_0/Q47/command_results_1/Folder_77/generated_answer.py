import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{100,169}', s[103:276]))
