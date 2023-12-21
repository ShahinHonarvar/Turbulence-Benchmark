import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{21,31}'.lower(), s[24:-84]))
