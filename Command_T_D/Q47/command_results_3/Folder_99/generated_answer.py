 
import re
def palindromes_of_specific_lengths(text):
    return set(re.findall(r'[a-z]{119,141}(?=\W)', text[127:288]))
