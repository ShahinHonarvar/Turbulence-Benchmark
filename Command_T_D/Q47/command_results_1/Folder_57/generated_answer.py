import re
def palindromes_of_specific_lengths(s):
    return set(map(str.lower, re.findall(r'((?=([a-z]+[a-z]+){2,5}[a-z]+)+)', s[16:94])))
