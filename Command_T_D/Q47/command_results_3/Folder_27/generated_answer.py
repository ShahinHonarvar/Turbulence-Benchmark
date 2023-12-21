import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{26,29}(?=\W|$)'.lower(), s[13:-100:]))
