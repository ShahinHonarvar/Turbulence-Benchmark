import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)([a-z]{3})([a-z]{4})([a-z]{3})', s[2:-2]))
