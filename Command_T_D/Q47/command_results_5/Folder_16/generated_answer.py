import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{51,60}(?i)(?=\W\1)', s[15:-15]))
