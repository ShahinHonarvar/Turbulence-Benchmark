import re
def palindromes_between_indices(s):
    return re.findall(r'(?i)(?=([^A-Za-z]+[A-Za-z]{4,6})[^A-Za-z]+)', s[3:-7])
