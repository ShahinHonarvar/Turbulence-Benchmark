 
import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{104,123}(?=\W[a-z]{119})[a-z]{104,123}', s))
