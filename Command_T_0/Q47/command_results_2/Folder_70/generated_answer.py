import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=([a-z]{24,52}){10,70}(?i)([a-z]{24,52})\1)', s))
