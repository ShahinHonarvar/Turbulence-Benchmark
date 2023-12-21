import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{3,4}(?=\W|$)'.lower(), s[1:-1]))
