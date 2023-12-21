import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=([a-z]{3,4}(?=a-z[a-z]))', s[1:-1]))
