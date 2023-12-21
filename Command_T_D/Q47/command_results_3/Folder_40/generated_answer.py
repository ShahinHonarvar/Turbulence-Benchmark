 
import re
def palindromes_of_specific_lengths(str):
    return re.findall(r'[a-z]+[a-z]+[a-z]+[a-z]+[a-z]+[a-z]+', str[0:5], flags=re.I)
