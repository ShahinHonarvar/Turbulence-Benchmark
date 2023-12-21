import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=([a-z]{7,9}){75,95}(?i)([a-z]{7,9})', s))
