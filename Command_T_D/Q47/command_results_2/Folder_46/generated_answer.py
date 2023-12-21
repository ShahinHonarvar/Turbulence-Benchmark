 
import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{29,62}(?=\w)', s[11:97], flags=re.I))
