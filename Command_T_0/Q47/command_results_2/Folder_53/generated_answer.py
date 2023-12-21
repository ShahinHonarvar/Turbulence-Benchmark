import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=([a-z]+\1){3,10}(?i)([a-z]+\1){3,10})', s[1:300]))
