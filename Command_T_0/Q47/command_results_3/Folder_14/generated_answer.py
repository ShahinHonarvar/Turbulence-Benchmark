import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=([a-z]{6,8}[a-z]{6,8})\1)', s[10:-5:-1]))
