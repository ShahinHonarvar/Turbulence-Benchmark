import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=([a-z]{32}|{33}|{34}))\1+', s[23:-1]))
