 
import re
def palindromes_of_specific_lengths(text):
    return re.findall(r'[a-z]{31,32}(?i)[a-z]{23,24}(?i)[a-z]{23,24}(?i)[a-z]{32,33}(?i)[a-z]{23,24}(?i)[a-z]{32,33}(?i)[a-z]{31,32}(?i)', text)
