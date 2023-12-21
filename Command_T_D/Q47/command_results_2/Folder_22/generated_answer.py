 
import re
def palindromes_of_specific_lengths(text):
    return re.findall(r'(?i)(?=([a-z]+\d){4}[a-z]+)', text[100:-100])
