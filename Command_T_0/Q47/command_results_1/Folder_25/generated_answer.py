import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{30,46}(?=\W|$)', s[26:-84].lower()))
