 
import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{3,5}([a-z]+){3,5}([a-z]{3,5})', s.lower()))
