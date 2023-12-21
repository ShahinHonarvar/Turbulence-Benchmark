 
import re
def palindromes_of_specific_lengths(s):
    m = re.findall(r'[a-z]+\d{4,5}', s[11:87])
    return set(m)
