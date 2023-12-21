 
import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]+'.lower(), s[0:6]))
