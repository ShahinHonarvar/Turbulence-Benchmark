import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?<=.)[a-z]{4,5}(?=.)', s[63:-1]))
