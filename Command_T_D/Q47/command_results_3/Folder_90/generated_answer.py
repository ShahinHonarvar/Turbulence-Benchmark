 
import re
def palindromes_of_specific_lengths(s):
    return set(re.findall(r'[a-z]{1,}(?=\w)[a-z]{1,}\1', s[106:280].lower()))
