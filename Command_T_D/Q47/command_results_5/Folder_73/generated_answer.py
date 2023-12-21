 
import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{1,2}(?:[a-z]{1,}){22}(?:[a-z]{1,}){33}[a-z]{1,2}', s, flags=re.I))
