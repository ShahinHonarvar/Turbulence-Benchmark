 
import re
def palindromes_of_specific_lengths(text):
    return set(re.findall(r'[A-Z]{1,}(?=\S{1,})[A-Z]{1,}', text[103:-5:2], flags=re.I))
