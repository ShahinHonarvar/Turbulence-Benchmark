 
import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'(?i)(?=([^aieouAEIOU]{%d,%d}[aieouAEIOU])\1{%d,%d}[aieouAEIOU]{%d,%d})' % (50, 100, 50, 100), s))
