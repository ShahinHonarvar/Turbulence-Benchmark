import re
def palindromes_of_specific_lengths(s):
    return re.findall(r'(?i)([a-z]{18})([a-z]{18})', s[26:-1])
