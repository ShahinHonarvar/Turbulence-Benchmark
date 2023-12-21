 
import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]+(?=([23-77])[a-z]+[23-77])', s, flags=re.I))
