 
import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]+\d+\d\1', s[22:-22], flags=re.I))
