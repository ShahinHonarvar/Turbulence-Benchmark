import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)([a-z]{43})([a-z]{4})([a-z]{43})', s[16:78]))
