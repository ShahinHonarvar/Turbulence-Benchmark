import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=([a-z]{4,5}[a-z]{4,5})\1)', s[11:-6]))
