import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{23,39}(?=\W|$)', s[31:-1]))
