import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=([a-z]{3,4}){2})([a-z]{3,4})', s))
