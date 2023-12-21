 
import re
def palindromes_of_specific_lengths(s):
    return re.findall(r'[a-z]+[a-z]+', s[24:84])
