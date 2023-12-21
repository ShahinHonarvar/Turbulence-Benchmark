 
import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{39,52}', s[16:94]))
