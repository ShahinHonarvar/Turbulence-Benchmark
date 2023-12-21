import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=([a-z]){26}(?:[a-z]){2})[a-z]{2})([a-z]){26}(?:[a-z]){2})', s[13:-100]))
