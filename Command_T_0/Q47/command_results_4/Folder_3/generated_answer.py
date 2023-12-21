import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{49,51}', s[27:95]))
