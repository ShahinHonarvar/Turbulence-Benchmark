import re
def palindromes_of_specific_lengths(s):
    r = set(re.findall(r"((?=.*[a-z]))[a-z]+((?=.*[a-z]))", s[27:-5:2], flags=re.I))
    return r
