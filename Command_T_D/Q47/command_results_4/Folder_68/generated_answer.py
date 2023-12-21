 
import re
def palindromes_of_specific_lengths(text):
    return set(re.findall(r'(?i)(?=([a-z]){50}(?i)([a-z]{50}){100}(?i)([a-z]){50}(?i)[a-z]{50})', text))
