import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{12,14}(?=\W)', s[18:-2]))
