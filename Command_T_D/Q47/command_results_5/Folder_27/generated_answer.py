 
import re
def palindromes_of_specific_lengths(s):
    return re.findall(r'(?i)(?=([a-z]{26,29}))', s[13:-99])
