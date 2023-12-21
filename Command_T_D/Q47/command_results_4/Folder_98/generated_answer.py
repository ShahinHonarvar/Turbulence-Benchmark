import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{5,80}(?=([a-z]))', s, flags=re.I))
