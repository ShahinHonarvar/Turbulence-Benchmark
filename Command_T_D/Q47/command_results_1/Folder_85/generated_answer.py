 
import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{6,9}', s[29:-29]))
