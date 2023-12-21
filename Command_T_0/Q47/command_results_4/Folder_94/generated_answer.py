import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]+\d{5}([a-z]+)', s[40:-5]))
