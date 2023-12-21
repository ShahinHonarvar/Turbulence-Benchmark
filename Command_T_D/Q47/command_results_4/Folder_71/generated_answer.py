import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{18}([a-z]+){18}'.upper(), s[18:-18]))
