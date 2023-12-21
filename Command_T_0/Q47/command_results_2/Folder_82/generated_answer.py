import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{30,300}(?=\W)[a-z]{30,300}(?=\W)', s[3:-300:]))
