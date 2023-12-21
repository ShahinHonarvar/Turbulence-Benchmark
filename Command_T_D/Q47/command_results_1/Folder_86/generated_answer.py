import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{34,55}(?=\W|$)', s[30:-5]))
