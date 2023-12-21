 
import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{18,74}(?=([a-z]{15}|[a-z]{94}))', s.lower()))
