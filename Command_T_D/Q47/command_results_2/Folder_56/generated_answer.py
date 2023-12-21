 
import re
def palindromes_of_specific_lengths(text):
    return set(re.findall(r'[a-z]+[a-z]+[a-z]+[a-z]+[a-z]+[a-z]+[a-z]+[a-z]+[a-z]+', text[1:9]))
