 
import re
def palindromes_of_specific_lengths(s):
    return re.findall(r'(?i)(?=([a-z]+?)\1)', s[13:95])
